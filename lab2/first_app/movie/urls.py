from django.urls import path
from .views import movies_list, movie_create, movie_detail

app_name = 'movie'

urlpatterns = [
    path('list', movies_list, name='list'),
    path('movie/create', movie_create, name='create'),
    path('movie/delete/<int:pk>', movie_detail, name='delete'),
    path('movie/<int:pk>', movie_detail, name='detail'),

]
 