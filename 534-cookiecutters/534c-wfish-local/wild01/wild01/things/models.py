from django.db import models
from django.urls import reverse


class Thing(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        ordering = (
            "name",
            "pk",
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("things:detail", args=[str(self.id)])
