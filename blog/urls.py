from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food', views.food, name='food'),

    path('editor', views.editor, name='editor'),
]
