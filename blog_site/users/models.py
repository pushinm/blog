from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _


# Create your models here.

class MyCustomUser(AbstractUser):
    groups = models.ForeignKey(to='MyCustomUserGroup', on_delete=models.DO_NOTHING, related_name='users_group')


class MyCustomUserGroup(Group):
    is_admin = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
