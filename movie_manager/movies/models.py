from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)


class Genre(models.Model):
    name = models.CharField(max_length=255)

class Actor(models.Model):
    name = models.CharField(max_length=255)

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.PositiveIntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


