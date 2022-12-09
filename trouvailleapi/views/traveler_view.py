from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Traveler

class TravelerView(ViewSet):
    """Viewset for travelers"""

    def retrieve(self, request, pk):
        """Handle GET requests for single traveler

        Returns:
            Response -- JSON serialized traveler
        """
        try:
            traveler = Traveler.objects.get(pk=pk)
            serializer = TravelerSerializer(traveler)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all travelers

        Returns:
            Response -- JSON serialized list of travelers
        """

        travelers = Traveler.objects.all()
        serializer = TravelerSerializer(travelers, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an traveler

        Returns:
            Response -- Empty body with 204 status code
        """

        traveler = Traveler.objects.get(user=request.auth.user)
        traveler.bio = request.data["bio"]
        traveler.profile_image_url = request.data["profileImg"]

        user = request.auth.user
        user.last_name = request.data["lastName"]
        user.first_name = request.data["firstName"]
        user.username = request.data["username"]

        traveler.save()
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TravelerSerializer(serializers.ModelSerializer):
    """JSON serializer for travelers"""
    
    class Meta:
        model = Traveler
        fields = ('id', 'full_name', 'username', 'bio', 'profile_image_url')