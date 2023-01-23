from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField


class SiteUser(AbstractUser):
    phonenumber = PhoneNumberField(required=True, unique=True)

    class Meta:
        ordering = ['first_name', 'last_name',
                    'phonenumber', 'email', 'username', 'password']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
