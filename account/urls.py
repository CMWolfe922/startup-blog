
from django.urls import path, include
from django.conf import settings
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
