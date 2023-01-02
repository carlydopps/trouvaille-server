from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from trouvailleapi.models import FavoriteTrip, Traveler, Trip

class FavoriteTripView(ViewSet):
    """Viewset for favorite trips"""

    def retrieve(self, request, pk):
        """Handle GET requests for single favorite trip

        Returns:
            Response -- JSON serialized favorite trip
        """
        try:
            favorite_trip = FavoriteTrip.objects.get(pk=pk)
            serializer = FavoriteTripSerializer(favorite_trip)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all favorite trips

        Returns:
            Response -- JSON serialized list of favorite trips
        """

        favorite_trips = FavoriteTrip.objects.all()
        serializer = FavoriteTripSerializer(favorite_trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an favorite trip

        Returns
            Response -- JSON serialized favorite trip instance
        """
        traveler = Traveler.objects.get(user=request.auth.user)
        trip = Trip.objects.get(pk=request.data['tripId'])

        favorite_trip = FavoriteTrip.objects.create(
            traveler = traveler,
            trip = trip
        )
        serializer = FavoriteTripSerializer(favorite_trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an favorite trip

        Returns:
            Response -- Empty body with 204 status code
        """

        favorite_trip = FavoriteTrip.objects.get(pk=pk)
        favorite_trip.traveler = Traveler.objects.get(user=request.auth.user)
        favorite_trip.trip = Trip.objects.get(pk=request.data['tripId'])

        favorite_trip.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['delete'], detail=True)
    def unfavorite(self, request, pk):
        """ Delete request for a favorite trip"""
        traveler = Traveler.objects.get(user=request.auth.user)
        trip = Trip.objects.get(pk=request.query_params['trip'])
        favorite_trip = FavoriteTrip.objects.get(traveler=traveler, trip=trip)
        favorite_trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class TravelerSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite trip's traveler"""

    class Meta:
            model = Traveler
            fields = ('id', 'full_name', 'profile_img')

class FavoriteTripSerializer(serializers.ModelSerializer):
    """JSON serializer for favorite_trips"""

    traveler = TravelerSerializer(many=False)
    
    class Meta:
        model = FavoriteTrip
        fields = ('id', 'trip', 'traveler')