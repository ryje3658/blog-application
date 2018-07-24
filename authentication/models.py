from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


"""Extending Default Django User Class with Profile/Attributes"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    location_city = models.CharField(max_length=255, blank=True, null=True)
    location_state = models.CharField(max_length=255, blank=True, null=True)
    location_country = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=2500, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)


    def __str__(self):
    	return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

