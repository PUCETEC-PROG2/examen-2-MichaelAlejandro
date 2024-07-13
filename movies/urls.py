from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/<int:movies_id>/", views.Movies, name="movie"),
]