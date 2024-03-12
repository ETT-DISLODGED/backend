from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Voice_Info, User

@receiver(post_save, sender=User)
def creat_voice_info(sender, instance, created, **kwargs):

    if created:
        Voice_Info.objects.create(user=instance)