from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en','audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url','description')

admin.site.register(Movie, MovieAdmin)

    # title = models.CharField(max_length=10)
    # title_en = models.CharField(max_length=10)
    # audience = models.IntegerField()
    # open_date = models.DateTimeField(auto_now_add=True)
    # genre = models.CharField(max_length=10)
    # watch_grade = models.CharField(max_length=10)
    # score = models.FloatField()
    # description = models.CharField(max_length=1000)