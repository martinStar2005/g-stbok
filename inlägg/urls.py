
from django.urls import path
from inlägg import views


urlpatterns = [
    path('', views.index, name='index'),
]
