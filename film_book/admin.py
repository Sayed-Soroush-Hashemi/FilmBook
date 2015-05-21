from django.contrib import admin
from film_book.models import Movie, Post, Comment, Crew, Role, Rate
# Register your models here.

admin.site.register(Movie)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Crew)
admin.site.register(Role)
admin.site.register(Rate)
