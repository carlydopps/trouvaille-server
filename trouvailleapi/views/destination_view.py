from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Destination
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class DestinationPermission(permissions.BasePermission):
    """Custom permissions for destination view"""

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'destroy']:
            return request.auth is not None
        else:
            return False

class DestinationView(ViewSet):
    """Viewset for destinations"""

    permission_classes = [DestinationPermission]

    def retrieve(self, request, pk):
        """Handle GET requests for single destination

        Returns:
            Response -- JSON serialized destination
        """
        try:
            destination = Destination.objects.get(pk=pk)
            serializer = DestinationSerializer(destination)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all destinations

        Returns:
            Response -- JSON serialized list of destinations
        """

        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an destination

        Returns
            Response -- JSON serialized destination instance
        """

        destination = Destination.objects.create(
            city = request.data["city"],
            state = request.data["state"],
            country = request.data["country"]
        )
        serializer = DestinationSerializer(destination)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an destination

        Returns:
            Response -- Empty body with 204 status code
        """

        destination = Destination.objects.get(pk=pk)
        destination.city = request.data["city"]
        destination.state = request.data["state"]
        destination.country = request.data["country"]

        destination.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        destination = Destination.objects.get(pk=pk)
        destination.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class DestinationSerializer(serializers.ModelSerializer):
    """JSON serializer for destinations"""
    
    class Meta:
        model = Destination
        fields = ('id', 'city', 'state', 'country')