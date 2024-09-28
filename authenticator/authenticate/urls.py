from django.urls import path
from . import views

urlpatterns = [
    path('views/', view=views.site.urls),
]
