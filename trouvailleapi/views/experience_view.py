from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from trouvailleapi.models import Experience, ExperienceType
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class ExperiencePermission(permissions.BasePermission):
    """Custom permissions for experience view"""

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'destroy']:
            return request.auth is not None
        else:
            return False

class ExperienceView(ViewSet):
    """Viewset for experiences"""

    permission_classes = [ExperiencePermission]

    def retrieve(self, request, pk):
        """Handle GET requests for single experience

        Returns:
            Response -- JSON serialized experience
        """
        try:
            experience = Experience.objects.get(pk=pk)
            serializer = ExperienceSerializer(experience)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all experiences

        Returns:
            Response -- JSON serialized list of experiences
        """

        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an experience

        Returns
            Response -- JSON serialized experience instance
        """
        experience_type = ExperienceType.objects.get(pk=request.data["experienceTypeId"])

        experience = Experience.objects.create(
            title = request.data["title"],
            address = request.data["address"],
            website_url = request.data["websiteUrl"],
            experience_type = experience_type
        )
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an experience

        Returns:
            Response -- Empty body with 204 status code
        """

        experience = Experience.objects.get(pk=pk)
        experience.title = request.data["title"]
        experience.address = request.data["address"]
        experience.website_url = request.data["websiteUrl"]

        experience_type = ExperienceType.objects.get(pk=request.data["experienceTypeId"])
        experience.experience_type = experience_type
        experience.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        experience = Experience.objects.get(pk=pk)
        experience.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class ExperienceTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for experiences"""

    class Meta:
        model = ExperienceType
        fields = ('id', 'name')

class ExperienceSerializer(serializers.ModelSerializer):
    """JSON serializer for experiences"""

    experience_type = ExperienceTypeSerializer(many=False)
    
    class Meta:
        model = Experience
        fields = ('id', 'title', 'address', 'website_url', 'experience_type')