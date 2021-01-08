from django.db import models
from django.utils.text import slugify


class Countries(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre")
    slug = models.SlugField(max_length=200, verbose_name='slug',
                            blank=True, null=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
