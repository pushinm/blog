from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from ...models import MyCustomUserGroup


class Command(BaseCommand):
    help = 'create a new custom group'

    def handle(self, *args, **kwargs):
        group, created = MyCustomUserGroup.objects.get_or_create(name='custom_group')
        if created:
            permissions = Permission.objects.all()
            group.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS(f'Group {group.name} has been created'))
        else:
            self.stdout.write(self.style.WARNING(f'Group {group.name} already exists'))
