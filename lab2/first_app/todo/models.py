from tabnanny import verbose
from turtle import update
from unicodedata import name
from django.db import models
from django.forms import CharField
from django.test import modify_settings

class Todo(models.Model):
    name=models.fields.CharField(verbose_name="Todo Name",max_length=100,unique=True)
    priority=models.fields.IntegerField(verbose_name="Todo priority",default=1)
    todo_date=models.fields.DateField(verbose_name="Date ",default='2000-01-01')
    is_done=models.fields.BooleanField(default=False)
    notes=models.fields.TextField(default='')
    creation_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Todo'
        verbose_name_plural='Todos'
        ordering= ('-id',)




class Tasks (models.Model):
    name=models.fields.CharField(verbose_name="Task Name",max_length=100)
    todo=models.ForeignKey('todo',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"Task {self.id} For Todo : {self.todo.name}"
# class Actor(models.Model):
#     pass

# class Movie(models.Model):
#     actors=models.ManyToManyField('actor')
#     director=models.ManyToManyField('director')
#     serial_number=models.OneToOneField('serial')
#     class Meta:
#         verbose_name='Movie'
#         verbose_name_plural='Movies'

# class Director(models.Model):
#     # da byt3ml m3 migration
#     user=models.ForeignKey('user')

# class serial(models.Model):
#     serial_key=models.CharField(max_length=50)