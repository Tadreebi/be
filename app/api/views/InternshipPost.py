from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, filters
from app.models.InternshipPost import PostInternship
from app.api.serializers.InternshipPost import PostSerializer

# List and Create == GET and POST
class PostInternshipList(APIView):
    def get(self, request):
        posts = PostInternship.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED,
                )
        return Response(
            serializer.data,
            status = status.HTTP_400_BAD_REQUEST,
        )