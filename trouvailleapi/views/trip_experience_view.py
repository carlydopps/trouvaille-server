from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from datetime import datetime
from trouvailleapi.models import Trip, Experience, TripExperience

class TripExperienceView(ViewSet):
    """Viewset for trip experiences"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip experience

        Returns:
            Response -- JSON serialized trip experience
        """
        try:
            trip_experience = TripExperience.objects.get(pk=pk)
            serializer = TripExperienceSerializer(trip_experience)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all trip experiences

        Returns:
            Response -- JSON serialized list of trip experiences
        """

        trip_experiences = TripExperience.objects.all()
        serializer = TripExperienceSerializer(trip_experiences, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        """Handle POST operations for a trip experience

        Returns
            Response -- JSON serialized trip experience instance
        """
        trip = Trip.objects.get(pk=request.data["tripId"])
        experience = Experience.objects.get(pk=request.data["experienceId"])

        trip_experience = TripExperience.objects.create(
            trip = trip,
            experience = experience
        )

        serializer = TripExperienceSerializer(trip_experience)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TripExperienceSerializer(serializers.ModelSerializer):
    """JSON serializer for trip experiences"""
    
    class Meta:
        model = TripExperience
        fields = ('id', 'trip', 'experience')