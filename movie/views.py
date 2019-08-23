from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):
    movie = Movie.objects.order_by('id')
    context = {
        'movie': movie
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'movie/detail.html', context)

def create(request):
    # 저장 로직
    # 'title', 'title_en','audience', 'open_date', 'genre', 'watch_grade', 
    # 'score', 'poster_url','description'
    title = request.GET.get('title')
    title_en = request.GET.get('title_en')
    audience = request.GET.get('audience')
    open_date = request.GET.get('open_date')
    genre = request.GET.get('genre')
    watch_grade = request.GET.get('watch_grade')
    score = request.GET.get('score')
    poster_url = request.GET.get('poster_url')
    description = request.GET.get('description')

    movie = Movie(
        title=title, 
        title_en=title_en,
        audience=audience,
        open_date=open_date,
        genre=genre,
        watch_grade=watch_grade,
        score=score,
        poster_url=poster_url,
        description=description,
        )
    movie.save()
    # context = {
    #     'article': article
    # }
    # return render(request, 'articles/create.html', context)
    return redirect(f'/movie/{movie.pk}/')