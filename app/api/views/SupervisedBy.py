from rest_framework import generics, permissions
from app.models import SupervisedBy
from app.api.serializers import SupervisedBySerializer


class SupervisedByListView(generics.ListCreateAPIView):
    queryset = SupervisedBy.objects.all()
    serializer_class = SupervisedBySerializer
    permission_classes = [permissions.IsAuthenticated]


class SupervisedByDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupervisedBy.objects.all()
    serializer_class = SupervisedBySerializer
    permission_classes = [permissions.IsAuthenticated]
