from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Blogger


def blogger_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="blogger")
        instance.groups.add(group)
        Blogger.objects.create(
            user=instance,
            name=instance.username
        )

        print("Profile created")


post_save.connect(blogger_profile, sender=User)
