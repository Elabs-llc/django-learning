from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('about', view=views.about, name='about'),
    path('delete/<list_id>', view=views.delete, name='delete'),
    path('complete/<list_id>', view=views.complete, name='complete'),
    path('uncomplete/<list_id>', view=views.uncomplete, name='uncomplete'),
    path('edit/<list_id>', view=views.edit, name='edit')


]
