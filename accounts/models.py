from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.CharField(max_length=120, verbose_name="User")
    email = models.CharField(max_length=120, verbose_name="Email")

    name = models.CharField(max_length=120, verbose_name="İsim")
    surname = models.CharField(max_length=120, verbose_name="Soyisim")
    address = models.TextField(verbose_name="Adres")

    def __str__(self):
        return f" {self.name} {self.surname} "

    class Meta:
        verbose_name = 'Kullanıcı Profili'
        verbose_name_plural = 'Kullanıcı Profili'
