from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, filters
from app.models.InternshipPost import PostInternship
from app.api.serializers.InternshipPost import PostSerializer
from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)


# GET and POST
class PostInternshipList(ListCreateAPIView):
    queryset = PostInternship.objects.all()
    serializer_class = PostSerializer

# GET DELETE PUT
class PostInternshipRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = PostInternship.objects.all()
    serializer_class = PostSerializer


# # List and Create == GET and POST
# class PostInternshipList(APIView):
#     def get(self, request):
#         posts = PostInternship.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status = status.HTTP_201_CREATED,
#                 )
#         return Response(
#             serializer.data,
#             status = status.HTTP_400_BAD_REQUEST,
#         )

# # GET PUT DELETE
# class PostInternshipDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return PostInternship.objects.get(pk=pk)
#         except PostInternship.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         posts = self.get_object(pk)
#         serializer = PostSerializer(posts)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         posts = self.get_object(pk)
#         serializer = PostSerializer(posts, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         posts = self.get_object(pk)
#         posts.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)