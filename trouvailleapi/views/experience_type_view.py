from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import ExperienceType

class ExperienceTypeView(ViewSet):
    """Viewset for experience types"""

    def retrieve(self, request, pk):
        """Handle GET requests for single experience type

        Returns:
            Response -- JSON serialized experience type
        """
        try:
            experienceType = ExperienceType.objects.get(pk=pk)
            serializer = ExperienceTypeSerializer(experienceType)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all experience types

        Returns:
            Response -- JSON serialized list of experience types
        """

        experienceTypes = ExperienceType.objects.all()
        serializer = ExperienceTypeSerializer(experienceTypes, many=True)
        return Response(serializer.data)

class ExperienceTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for experiences"""
    
    class Meta:
        model = ExperienceType
        fields = ('id', 'name')