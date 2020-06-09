from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm, NewsForm
from django.contrib.auth.decorators import login_required

class Login(LoginView):
    form_class = LoginForm
    template_name = 'system/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'system/login.html'


@login_required
def index(request):
    return render(request, 'system/index.html')


def news(request):
    form = NewsForm()
    return render(request, 'system/news.html', {'form': form})