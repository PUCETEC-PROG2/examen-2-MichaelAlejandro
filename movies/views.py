
from django.http import HttpResponse
from django.template import loader
from .models import Movies

def index(request):
    Movies = Movies.objects.order_by('gender')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))

def movie(request, movies_id):
    movies = Movies.objects.get(pk= movies_id)
    template = loader.get_template('display_movies.html')
    context = {
        'movie': movies
    }
    return HttpResponse(template.render(context, request))