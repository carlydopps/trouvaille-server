from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Duration

class DurationView(ViewSet):
    """Viewset for durations"""

    def retrieve(self, request, pk):
        """Handle GET requests for single duration

        Returns:
            Response -- JSON serialized duration
        """
        try:
            duration = Duration.objects.get(pk=pk)
            serializer = DurationSerializer(duration)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all durations

        Returns:
            Response -- JSON serialized list of durations
        """

        durations = Duration.objects.all()
        serializer = DurationSerializer(durations, many=True)
        return Response(serializer.data)

class DurationSerializer(serializers.ModelSerializer):
    """JSON serializer for durations"""
    
    class Meta:
        model = Duration
        fields = ('id', 'extent')