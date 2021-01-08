from django.db import models
from django.utils.text import slugify

from apps.albums.models import Albums


class Songs(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="nombre")
    slug = models.SlugField(max_length=200, verbose_name='slug',
                            blank=True, null=True)
    duration = models.PositiveIntegerField(verbose_name="duración")
    album = models.ForeignKey(Albums, on_delete=models.CASCADE,
                              verbose_name="album")

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
