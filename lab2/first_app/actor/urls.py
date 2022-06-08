from django.urls import path 
from .views import actors_list,actor_details,actor_create,actor_delete,actor_update


app_name='actor'

urlpatterns=[
    path('list',actors_list ,name= 'list'),
    path('create', actor_create, name='create'),
    path('update/<int:pk>',actor_update, name='update'),
    path('actor/<int:pk>', actor_details, name='details'),
    path('actor/delete/<int:pk>', actor_delete, name='delete')
   

]