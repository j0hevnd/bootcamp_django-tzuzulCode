from tabnanny import verbose
from unicodedata import numeric
from django.db import models

from apps.movies.models import Movie


class Review(models.Model):
    comment = models.TextField('Comment', blank=False, null=False)
    movie_review = models.ForeignKey(Movie, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modification_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['movie_review__id']

    def __str__(self):
        return f"{self.id} - {self.movie_review.movie_name}"
