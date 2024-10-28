from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from userApp.models import Xodim


class Qabul(models.Model):
    yil = models.DateField()
    kvota = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    budjet_k = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    kantrak_k = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    budjet_b = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(200)])
    kantrak_b = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(200)])

    def __str__(self):
        return f'{self.yil} - {self.kvota}'

    class Meta:
        verbose_name = 'Qabul'
        verbose_name_plural = 'Qabullar'
        ordering = ('-yil',)


class Yonalish(models.Model):
    nomi = models.CharField(max_length=255)
    malumot = models.TextField(blank=True, null=True)
    qabul = models.ForeignKey(Qabul, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Yonalish'
        verbose_name_plural = 'Yonalishlar'
        ordering = ('nomi',)


class Kafedra(models.Model):
    nomi = models.CharField(max_length=255)
    xona_raqami = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    xodimlar = models.ForeignKey(Xodim, on_delete=models.CASCADE, default=1)
    yonalishlar = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Kafedra'
        verbose_name_plural = 'Kafedralar'
        ordering = ('nomi',)

class Lokatsiya(models.Model):
    mamlakat = models.CharField(max_length=100)
    viloyat = models.CharField(max_length=100)
    shahar = models.CharField(max_length=100)  # Shahar yoki qishloq nomi
    manzil = models.TextField(blank=True, null=True)  # Aniq manzil (ko'cha, uy raqami va h.k.)
    zip_kod = models.CharField(max_length=10, blank=True, null=True)  # Zip yoki pochta kodi

    def __str__(self):
        return f"{self.mamlakat}, {self.viloyat}, {self.shahar}"

class Fakultet(models.Model):
    nomi = models.CharField(max_length=255)
    kafedralar = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logo')
    lokatsiya = models.ForeignKey(Lokatsiya, on_delete=models.SET_NULL, null=True, blank=True)  # Fakultetning lokatsiyasi

    def __str__(self):
        return self.nomi

class Rektorad(models.Model):
    xodim = models.ForeignKey(Xodim, on_delete=models.CASCADE)
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    malumoti = models.TextField()
    logo = models.ImageField(upload_to='logo')
    email = models.EmailField()
    tel = models.CharField(max_length=15)




