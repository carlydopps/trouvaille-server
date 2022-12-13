from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from datetime import datetime
from trouvailleapi.models import Trip, Destination, TripDestination

class TripDestinationView(ViewSet):
    """Viewset for trip destinations"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip destination

        Returns:
            Response -- JSON serialized trip destination
        """
        try:
            trip_destination = TripDestination.objects.get(pk=pk)
            serializer = TripDestinationSerializer(trip_destination)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all trip destinations

        Returns:
            Response -- JSON serialized list of trip destinations
        """

        trip_destinations = TripDestination.objects.all()
        serializer = TripDestinationSerializer(trip_destinations, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        """Handle POST operations for a trip destination

        Returns
            Response -- JSON serialized trip destination instance
        """
        trip = Trip.objects.get(pk=request.data["tripId"])
        destination = Destination.objects.get(pk=request.data["destinationId"])

        trip_destination = TripDestination.objects.create(
            trip = trip,
            destination = destination
        )

        serializer = TripDestinationSerializer(trip_destination)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TripDestinationSerializer(serializers.ModelSerializer):
    """JSON serializer for trip destinations"""
    
    class Meta:
        model = TripDestination
        fields = ('id', 'trip', 'destination')