from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from trouvailleapi.models import Comment, Traveler, Trip

class CommentView(ViewSet):
    """Viewset for comments"""

    def retrieve(self, request, pk):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all comments

        Returns:
            Response -- JSON serialized list of comments
        """

        comments = Comment.objects.all().order_by('-id')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an comment

        Returns
            Response -- JSON serialized comment instance
        """
        traveler = Traveler.objects.get(user=request.auth.user)
        trip = Trip.objects.get(pk=request.data['tripId'])

        comment = Comment.objects.create(
            traveler = traveler,
            trip = trip,
            message = request.data['message']
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an comment

        Returns:
            Response -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.traveler = Traveler.objects.get(user=request.auth.user)
        comment.trip = Trip.objects.get(pk=request.data['tripId'])
        comment.message = request.data['message']

        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):

        traveler = Traveler.objects.get(user=request.auth.user)
        comment = Comment.objects.get(pk=pk)

        if traveler == comment.traveler:
            comment.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TravelerSerializer(serializers.ModelSerializer):
    """JSON serializer for comment's traveler"""

    class Meta:
            model = Traveler
            fields = ('id', 'first_name', 'profile_img')

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""

    traveler = TravelerSerializer(many=False)
    
    class Meta:
        model = Comment
        fields = ('id', 'trip', 'traveler', 'message')