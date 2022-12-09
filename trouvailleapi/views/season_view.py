from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Season

class SeasonView(ViewSet):
    """Viewset for seasons"""

    def retrieve(self, request, pk):
        """Handle GET requests for single season

        Returns:
            Response -- JSON serialized season
        """
        try:
            season = Season.objects.get(pk=pk)
            serializer = SeasonSerializer(season)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all seasons

        Returns:
            Response -- JSON serialized list of seasons
        """

        seasons = Season.objects.all()
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)

class SeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for seasons"""
    
    class Meta:
        model = Season
        fields = ('id', 'name')