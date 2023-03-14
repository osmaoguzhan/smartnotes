from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/notes/')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = '/notes/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/notes/')
        return super().get(request, *args, **kwargs)
