from django.db import models
from django.utils.text import slugify

from apps.countries.models import Countries


class Artists(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre", unique=True)
    slug = models.SlugField(max_length=200, verbose_name='slug',
                            blank=True, null=True)
    about = models.TextField(verbose_name="Acerca del Artista")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE,
                                verbose_name="País")

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

