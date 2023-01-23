from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.views.generic.base import LoginView, LogoutView, UserRegistrationView
from .forms import UserLoginForm, CustomUserRegistrationForm


# class UserLoginView(LoginView):
#     form_class = UserLoginForm
#     template_name = 'registration/login.html'


# class UserRegisterView(UserRegistrationView):
#     form_class = CustomUserRegistrationForm


@login_required
def homepage(request):
    return render(request, 'home.html', {'user': request.user.get_fullname()})
