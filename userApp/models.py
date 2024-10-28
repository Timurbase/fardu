from django.db import models
from django.contrib.auth.models import AbstractUser

class Xodim(AbstractUser):
    unvoni = models.CharField(max_length=255)
    lavozim = models.CharField(max_length=255)
    tel = models.CharField(max_length=14)
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Xodim'
        verbose_name_plural = 'Xodimlar'