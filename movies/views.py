# # ------------------------------------------
# # imports needed for the functional view
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # ------------------------------------------
#
# # ------------------------------------------
# # generics class to make writing endpoints easier
# from rest_framework import generics
# # ------------------------------------------


from . import models
from . import serializers

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class ListCreateMovies(APIView):
    def get(self, request, format=None):
        movies = models.Movies.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = serializers.MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def list_create_movies(request):
#     """
#     A function based view that use the api_view decorator to add functionality
#     to the view.
#     """
#     if request.method == 'GET':
#         movies = models.Movie.objects.all()
#         serializer = serializers.MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#
# class ListCreateMovies(generics.ListAPIView):
#     """
#     A class based view that inherits from the generics class. The generics
#     class gives you a convinient way to declare views quickly when you only
#     need basic functionality or simple CRUD operations.
#     """
#     queryset = models.Movie.objects.all()
#     serializer_class = serializers.MovieSerializer
