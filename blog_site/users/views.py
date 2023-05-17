from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import MyCustomUser, MyCustomUserGroup

@login_required
@user_passes_test(lambda u: u.groups.filter(name='custom_group').exists() or u.is_superuser)
def my_view(request):
    group = MyCustomUserGroup.objects.all()
    user = MyCustomUser.objects.all()
    user = request.user
    print(f'User {user.username} is authecticated: {user.is_authenticated}')
    print(f'User {user.username} groups: {",".join([group.name for group in user.groups.all()])}')