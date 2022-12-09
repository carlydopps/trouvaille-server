from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Trip, Traveler, Style, Season, Duration, Experience, Destination

class TripView(ViewSet):
    """Viewset for trips"""

    def retrieve(self, request, pk):
        """Handle GET requests for single trip

        Returns:
            Response -- JSON serialized trip
        """
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all trips

        Returns:
            Response -- JSON serialized list of trips
        """

        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an trip

        Returns
            Response -- JSON serialized trip instance
        """
        traveler = Traveler.objects.get(pk=request.data["travelerId"])
        style = Style.objects.get(pk=request.data["styleId"])
        season = Season.objects.get(pk=request.data["seasonId"])
        duration = Duration.objects.get(pk=request.data["durationId"])

        trip = Trip.objects.create(
            title = request.data["title"],
            summary = request.data["summary"],
            is_draft = request.data["isDraft"],
            is_upcoming = request.data["isUpcoming"],
            is_private = request.data["isPrivate"],
            modified_date = request.data["modifiedDate"],
            traveler = traveler,
            style = style,
            season = season,
            duration = duration
        )
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an trip

        Returns:
            Response -- Empty body with 204 status code
        """

        trip = Trip.objects.get(pk=pk)
        trip.title = request.data["title"]
        trip.summary = request.data["summary"]
        trip.is_draft = request.data["isDraft"]
        trip.is_upcoming = request.data["isUpcoming"]
        trip.is_private = request.data["isPrivate"]
        trip.modified_date = request.data["modifiedDate"]

        traveler = Traveler.objects.get(pk=request.data["travelerId"])
        style = Style.objects.get(pk=request.data["styleId"])
        season = Season.objects.get(pk=request.data["seasonId"])
        duration = Duration.objects.get(pk=request.data["durationId"])

        trip.traveler = traveler
        trip.style = style
        trip.season = season
        trip.duration = duration
        trip.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class TravelerSerializer(serializers.ModelSerializer):
    """JSON serializer for trip traveler"""

    class Meta:
        model = Traveler
        fields = ('id', 'full_name', 'profile_image_url')

class StyleSerializer(serializers.ModelSerializer):
    """JSON serializer for trip style"""

    class Meta:
        model = Style
        fields = ('id', 'name')

class SeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for trip season"""

    class Meta:
        model = Season
        fields = ('id', 'name')

class DurationSerializer(serializers.ModelSerializer):
    """JSON serializer for trip duration"""

    class Meta:
        model = Duration
        fields = ('id', 'extent')

class ExperienceSerializer(serializers.ModelSerializer):
    """JSON serializer for trip duration"""

    class Meta:
        model = Experience
        fields = ('id', 'title', 'address', 'website_url', 'experience_type')

class DestinationSerializer(serializers.ModelSerializer):
    """JSON serializer for trip duration"""

    class Meta:
        model = Destination
        fields = ('id', 'city', 'state', 'country')

class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips"""

    traveler = TravelerSerializer(many=False)
    style = StyleSerializer(many=False)
    season = SeasonSerializer(many=False)
    duration = DurationSerializer(many=False)
    experiences = ExperienceSerializer(many=True)
    destinations = DestinationSerializer(many=True)
    
    class Meta:
        model = Trip
        fields = ('id', 'title', 'summary', 'traveler', 'style', 'season', 'duration', 'is_draft', 'is_upcoming', 'is_private', 'modified_date', 'experiences', 'destinations')