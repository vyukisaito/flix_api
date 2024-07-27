from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission
from movies.models import Movie
from movies.serializer import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
