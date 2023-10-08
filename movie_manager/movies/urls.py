from django.urls import path
from .views import (
    GenreListCreateView, GenreDetailView,
    ActorListCreateView, ActorDetailView,
    MovieListCreateView, MovieDetailView,
    ReviewListCreateView, ReviewDetailView,
)

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),

    path('actors/', ActorListCreateView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),

    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
