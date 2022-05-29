from django.urls import path, include
from . import views

app_name = 'canapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
]