from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from trouvailleapi.models import Subscription, Traveler

class SubscriptionView(ViewSet):
    """Viewset for subscriptions"""

    def retrieve(self, request, pk):
        """Handle GET requests for single subscription

        Returns:
            Response -- JSON serialized subscription
        """
        try:
            subscription = Subscription.objects.get(pk=pk)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all subscriptions

        Returns:
            Response -- JSON serialized list of subscriptions
        """

        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an subscription

        Returns
            Response -- JSON serialized subscription instance
        """
        follower = Traveler.objects.get(user=request.auth.user)
        traveler = Traveler.objects.get(pk=request.data["travelerId"])

        subscription = Subscription.objects.create(
            follower = follower,
            traveler = traveler
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an subscription

        Returns:
            Response -- Empty body with 204 status code
        """

        subscription = Subscription.objects.get(pk=pk)
        subscription.follower = Traveler.objects.get(user=request.auth.user)
        subscription.traveler = Traveler.objects.get(pk=request.data["travelerId"])

        subscription.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['delete'], detail=True)
    def unsubscribe(self, request, pk):
        """ Delete request for a subscription"""
        traveler = Traveler.objects.get(pk=request.query_params['traveler'])
        follower = Traveler.objects.get(user=request.auth.user)
        subscription = Subscription.objects.get(traveler=traveler, follower=follower)
        subscription.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class SubscriptionSerializer(serializers.ModelSerializer):
    """JSON serializer for subscriptions"""
    
    class Meta:
        model = Subscription
        fields = ('id', 'follower', 'traveler')