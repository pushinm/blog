from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator


# Create your models here.


class Author(AbstractUser):
    GENDERS = (
        ('m', 'мужчина'),
        ('f', 'женщина'),
    )

    gender = models.CharField(choices=GENDERS, max_length=1)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    class Meta:
        permissions = [
            ('edit_own_article', 'Can edit own articles'),
        ]
