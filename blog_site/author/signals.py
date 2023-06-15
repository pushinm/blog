from .models import Profile, Author
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

my_signal = Signal()



@receiver(post_save, sender=Author)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print('hello')
    if created:
        Profile.objects.create(author=instance)
    if not created:
        instance.author_profile.save()


my_signal.connect(create_or_update_user_profile)