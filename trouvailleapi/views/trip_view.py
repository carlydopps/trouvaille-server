from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import action
from trouvailleapi.models import Trip, Traveler, Style, Season, Duration, Experience, Destination, ExperienceType, FavoriteTrip, Comment
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class TripPermission(permissions.BasePermission):
    """Custom permissions for destination view"""

    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['retrieve', 'create', 'update', 'destroy']:
            return request.auth is not None
        else:
            return False

class TripView(ViewSet):
    """Viewset for trips"""

    permission_classes = [TripPermission]

    def retrieve(self, request, pk):
        """Handle GET requests for single trip

        Returns:
            Response -- JSON serialized trip
        """

        try:
            trip = Trip.objects.get(pk=pk)
            auth_traveler = Traveler.objects.get(user=request.auth.user)
            if  trip.traveler == auth_traveler:
                trip.my_trip = True
            else:
                trip.my_trip = False
            
            matched_favorite = FavoriteTrip.objects.filter(trip=trip).filter(traveler=auth_traveler)
            if len(matched_favorite) == 0:
                trip.favorite = False
            else:
                trip.favorite = True

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

        if 'status' in request.query_params:
            if request.query_params["status"] == "created":
                traveler = Traveler.objects.get(user=request.auth.user)
                trips = trips.filter(traveler = traveler)
        
        if 'auth' in request.query_params:
            if request.query_params['auth'] == 'required':
                favorite_trips = FavoriteTrip.objects.all()
                auth_traveler = Traveler.objects.get(user=request.auth.user)

                for trip in trips:
                    matched_favorite = favorite_trips.filter(trip=trip).filter(traveler=auth_traveler)
                    if len(matched_favorite) == 0:
                        trip.favorite = False
                    else:
                        trip.favorite = True

        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for a trip

        Returns
            Response -- JSON serialized trip instance
        """
        traveler = Traveler.objects.get(user=request.auth.user)
        style = Style.objects.get(pk=request.data["styleId"])
        season = Season.objects.get(pk=request.data["seasonId"])
        duration = Duration.objects.get(pk=request.data["durationId"])

        trip = Trip.objects.create(
            title = request.data["title"],
            summary = request.data["summary"],
            is_draft = request.data['isDraft'],
            is_upcoming = request.data["isUpcoming"],
            is_private = request.data["isPrivate"],
            modified_date = timezone.now(),
            traveler = traveler,
            style = style,
            season = season,
            duration = duration
        )
        serializer = TripSerializer(trip)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a trip

        Returns:
            Response -- Empty body with 204 status code
        """

        trip = Trip.objects.get(pk=pk)
        trip.title = request.data["title"]
        trip.summary = request.data["summary"]
        trip.is_draft = request.data["isDraft"]
        trip.is_upcoming = request.data["isUpcoming"]
        trip.is_private = request.data["isPrivate"]
        trip.modified_date = timezone.now()

        traveler = Traveler.objects.get(user=request.auth.user)
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
        traveler = Traveler.objects.get(user=request.auth.user)
        trip = Trip.objects.get(pk=pk)
        if traveler == trip.traveler:
            trip.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(None, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(methods=['delete'], detail=True)
    def remove_destination(self, request, pk):
        """Delete request for an destination to be removed from a trip"""
    
        destination = Destination.objects.get(pk=request.query_params["destination"])
        trip = Trip.objects.get(pk=pk)
        trip.destinations.remove(destination)
        return Response({'message': 'Destination removed'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['delete'], detail=True)
    def remove_experience(self, request, pk):
        """Delete request for an experience to be removed from a trip"""
    
        experience = Experience.objects.get(pk=request.query_params["experience"])
        trip = Trip.objects.get(pk=pk)
        trip.experiences.remove(experience)
        return Response({'message': 'Experience removed'}, status=status.HTTP_204_NO_CONTENT)
        
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

class ExperienceTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for experience type of trip experience"""
    
    class Meta:
        model = ExperienceType
        fields = ('id', 'name')

class ExperienceSerializer(serializers.ModelSerializer):
    """JSON serializer for trip duration"""

    experience_type = ExperienceTypeSerializer(many=False)

    class Meta:
        model = Experience
        fields = ('id', 'title', 'address', 'website_url', 'experience_type')

class DestinationSerializer(serializers.ModelSerializer):
    """JSON serializer for trip duration"""

    class Meta:
        model = Destination
        fields = ('id', 'city', 'state', 'country')

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for trip comment"""

    traveler = TravelerSerializer(many=False)
    
    class Meta:
        model = Comment
        fields = ('id', 'trip', 'traveler', 'message')

class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips"""

    traveler = TravelerSerializer(many=False)
    style = StyleSerializer(many=False)
    season = SeasonSerializer(many=False)
    duration = DurationSerializer(many=False)
    experiences = ExperienceSerializer(many=True)
    destinations = DestinationSerializer(many=True)
    trip_comments = CommentSerializer(many=True)
    
    class Meta:
        model = Trip
        fields = ('id', 'title', 'summary', 'traveler', 'style', 'season', 'duration', 'is_draft', 'is_upcoming', 'is_private', 'modified_date', 'my_trip', 'favorite', 'experiences', 'destinations', 'trip_comments')