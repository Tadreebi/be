from rest_framework import viewsets
from app.models.InternshipPost import PostInternship
from app.api.serializers.InternshipPost import PostSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response



# GET and POST
class PostInternshipList(ListCreateAPIView):

    queryset =  PostInternship.objects.all()
    serializer_class = PostSerializer


    def list(self, request, *args, **kw):
        queries = request.query_params

        list_queries = {f'{query}': queries.get(query).upper() for query in queries if (query in ("education", "industry", "experience"))}

        queryset =  PostInternship.objects.filter (**list_queries) if list_queries else  PostInternship.objects.all()

        return Response({queryset.values()})
  


# GET DELETE PUT
class PostInternshipRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = PostInternship.objects.all()
    serializer_class = PostSerializer

# ViewSets
class PostsViewSets(viewsets.ModelViewSet):
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