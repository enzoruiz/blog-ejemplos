from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
