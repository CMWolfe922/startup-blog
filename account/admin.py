from django.contrib import admin
from .models import SiteUser, Profile
# Register your models here.


class accountAdmin(admin.ModelAdmin):

    class Meta:
        model = SiteUser
        ordering = ['first_name', 'last_name', 'username', 'email']


admin.site.register(SiteUser)
admin.site.register(Profile)
