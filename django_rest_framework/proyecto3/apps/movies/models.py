from django.db import models

# Create your models here.

class Category(models.Model):
    gender = models.CharField('Movie genre', unique=True, max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.gender


class Movie(models.Model):
    movie_name = models.CharField('Movie name', unique=True, max_length=200, blank=False, null=False)
    description = models.TextField('Description', blank=False, null=False)
    category = models.ManyToManyField(Category)
    public = models.BooleanField('Public?', default=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ['id']

    def __str__(self):
        return f"{self.id} - {self.movie_name}"