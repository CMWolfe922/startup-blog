from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType
from phonenumber_field.modelfields import PhoneNumberField


class SiteUser(AbstractUser):
    phonenumber = PhoneNumberField(required=True, unique=True)

    class Meta:
        verbose_name = "user"
        ordering = ['first_name', 'last_name',
                    'phonenumber', 'email', 'username', 'password']


class Profile(models.Model):
    user = models.OneToOneField(SiteUser, primary_key=True, verbose_name='user',
                                related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/images/profile_picture',
                                default='static/imgs/default_profile_picture.jpg')
