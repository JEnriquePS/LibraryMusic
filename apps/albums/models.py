from django.db import models
from django.utils.text import slugify

from apps.artists.models import Artists


class Albums(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="nombre")
    slug = models.SlugField(max_length=200, verbose_name='slug',
                            blank=True, null=True)
    # cover = models.ImageField() TODO
    description = models.TextField(verbose_name="descripción")
    year = models.DateField(verbose_name='año de lanzamiento')
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE,
                               verbose_name="artista")

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
