import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # para nao dar erro ao fazer o post
from genres.models import Genre


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) #pego a requisição do body e docodifico 
        # em utf-8 json.loads tranforma em dicionario
        new_genre = Genre(name=data['name'])
        new_genre.save() # salva no banco de dados
        return JsonResponse(
            {'id': new_genre.id, 'name': new_genre.name}, status=201,
            ) # status=201 
        #significa que foi criado com sucesso 

