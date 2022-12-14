from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Traveler, Subscription, Trip, FavoriteTrip
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class TravelerPermission(permissions.BasePermission):
    """Custom permissions for traveler view"""

    def has_permission(self, request, view):
        if view.action in ['list']:
            return True
        elif view.action in ['retrieve', 'create', 'update', 'destroy']:
            return request.auth is not None
        else:
            return False

class TravelerView(ViewSet):
    """Viewset for travelers"""

    permission_classes = [TravelerPermission]

    def retrieve(self, request, pk):
        """Handle GET requests for single traveler

        Returns:
            Response -- JSON serialized traveler
        """
        try:
            if pk == 'auth':
                traveler = Traveler.objects.get(user=request.auth.user)
            else:
                traveler = Traveler.objects.get(pk=pk)
            
            auth_traveler = Traveler.objects.get(user=request.auth.user)

            matched_subscription = Subscription.objects.filter(traveler=traveler).filter(follower=auth_traveler)
            if len(matched_subscription) == 0:
                traveler.following = False
            else:
                traveler.following = True

            if auth_traveler == traveler:
                traveler.myself = True
            else:
                traveler.myself = False
                
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
        subscriptions = Subscription.objects.all()

        if request.auth:
            auth_traveler = Traveler.objects.get(user=request.auth.user)
        else:
            auth_traveler = None

        for traveler in travelers:
            matched_subscription = subscriptions.filter(traveler=traveler).filter(follower=auth_traveler)
            if len(matched_subscription) == 0:
                traveler.following = False
            else:
                traveler.following = True
            if auth_traveler == traveler:
                traveler.myself = True
            else:
                traveler.myself = False
            
        if 'preview' in request.query_params:
            end = int(request.query_params['preview'])
            travelers = travelers[0:end]

        serializer = TravelerSerializer(travelers, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an traveler

        Returns:
            Response -- Empty body with 204 status code
        """

        traveler = Traveler.objects.get(user=request.auth.user)
        traveler.bio = request.data["bio"]
        traveler.profile_img = request.data["profileImg"]
        traveler.cover_img = request.data["coverImg"]

        user = request.auth.user
        user.last_name = request.data["lastName"]
        user.first_name = request.data["firstName"]
        user.username = request.data["username"]

        traveler.save()
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for traveler trips """

    class Meta:
        model = Trip
        fields = ('id', 'title', 'summary', 'cover_img', 'style', 'season', 'duration', 'is_draft', 'is_upcoming', 'is_private', 'modified_date', 'experiences', 'destinations')
        depth = 1

class FavoriteTripSerializer(serializers.ModelSerializer):
    """JSON serializer for traveler trips """

    trip = TripSerializer(many=False)

    class Meta:
        model = FavoriteTrip
        fields = ('id', 'trip', 'traveler')

class TravelerSerializer(serializers.ModelSerializer):
    """JSON serializer for travelers"""

    traveled_trips = TripSerializer(many=True)
    favorite_trips = FavoriteTripSerializer(many=True)
    
    class Meta:
        model = Traveler
        fields = ('id', 'first_name', 'last_name', 'full_name', 'username', 'bio', 'profile_img', 'cover_img', 'following', 'myself', 'follower_count', 'traveled_trips', 'favorite_trips')