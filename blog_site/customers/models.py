from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(User):
    second_phone = models.CharField(verbose_name='Второй номер телефона', max_length=12)
    telegram = models.CharField(verbose_name='Телеграм', max_length=50)

    class Meta(User.Meta):
        pass