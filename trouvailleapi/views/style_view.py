from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Style

class StyleView(ViewSet):
    """Viewset for styles"""

    def retrieve(self, request, pk):
        """Handle GET requests for single style

        Returns:
            Response -- JSON serialized style
        """
        try:
            style = Style.objects.get(pk=pk)
            serializer = StyleSerializer(style)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all styles

        Returns:
            Response -- JSON serialized list of styles
        """

        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data)

class StyleSerializer(serializers.ModelSerializer):
    """JSON serializer for styles"""
    
    class Meta:
        model = Style
        fields = ('id', 'name')