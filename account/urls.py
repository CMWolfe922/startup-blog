
from django.urls import path, include
from django.conf import settings
from .views import homepage

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('', homepage, name="home")
]
