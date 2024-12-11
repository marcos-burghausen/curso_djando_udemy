from django.http import HttpResponse
from recipies.views import home
from django.urls import path

urlpatterns = [
    path('', home),
]