from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from trouvailleapi.models import Image, Trip

class ImageView(ViewSet):
    """Viewset for images"""

    def retrieve(self, request, pk):
        """Handle GET requests for single image

        Returns:
            Response -- JSON serialized image
        """
        try:
            image = Image.objects.get(pk=pk)
            serializer = ImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all images

        Returns:
            Response -- JSON serialized list of images
        """

        images = Image.objects.all().order_by('trip', 'order')
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations for an image

        Returns
            Response -- JSON serialized image instance
        """
        trip = Trip.objects.get(pk=request.data["tripId"])

        image = Image.objects.create(
            trip = trip,
            img_url = request.data["imgUrl"],
            order = request.data["order"]
        )
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an image

        Returns:
            Response -- Empty body with 204 status code
        """

        image = Image.objects.get(pk=pk)
        image.trip = Trip.objects.get(pk=request.data["tripId"])
        image.img_url = request.data["imgUrl"]
        image.order = request.data["order"]
        image.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        image = Image.objects.get(pk=pk)
        image.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for images"""
    
    class Meta:
        model = Image
        fields = ('id', 'trip', 'img_url', 'order')