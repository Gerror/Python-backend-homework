from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


def login_required(function):
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        else:
            return function(self, request, *args, **kwargs)
    return wrapper

class HomeView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        return render(request, "home.html")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
