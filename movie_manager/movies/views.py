from rest_framework import generics
from .models import Genre, Actor, Movie, Review
from .serializers import GenreSerializer, ActorSerializer, MovieSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Фильтр для названия с учетом регистра
    genres = django_filters.ModelMultipleChoiceFilter(
        field_name='genres__name',
        to_field_name='name',
        queryset=Genre.objects.all(),
    )  # Фильтр для жанров

    class Meta:
        model = Movie
        fields = ['title', 'release_date']


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = PageNumberPagination


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]  # Добавляем фильтрацию
    filterset_class = MovieFilter  # Указываем класс фильтра
    pagination_class = PageNumberPagination


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
