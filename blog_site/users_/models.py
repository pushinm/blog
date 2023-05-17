from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20, verbose_name='Пароль', validators=[RegexValidator(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$',
        message='Пароль должен содержать не менее 8 символов и иметь по крайней мере одну строчную букву, одну заглавную букву и одну цифру!'
    )])
    age = models.DateField('год рождения')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
