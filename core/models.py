from django.db import models


class KeyVal(models.Model):
    objects = models.Manager()
    key = models.CharField(max_length=255)
    value = models.TextField()

    def __str__(self) -> str:
        return str(self.key)
