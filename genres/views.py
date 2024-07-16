import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # para nao dar erro ao fazer o post
from django.shortcuts import get_object_or_404
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer


class GenreCreatListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    ...


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name'] # o name vai receber um novo name
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name': genre.name}
        )

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message': 'Gênero excluido com sucesso'},
            status=204, # ao deletar um  objeto atraves de uma api rest o padrao é retornar um status204
        )
    