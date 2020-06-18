from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm, NewsForm
from django.contrib.auth.decorators import login_required
from site2.models import News

class Login(LoginView):
    form_class = LoginForm
    template_name = 'system/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'system/login.html'


@login_required
def index(request):
    return render(request, 'system/index.html')


# 新着情報の一覧
@login_required
def news(request):
    news = News.objects.all()
    return render(request, 'system/news.html', {'news': news,})


# 新着情報の新規作成
@login_required
def news_add(request):
    if request.method == 'POST':
        obj = News()
        form = NewsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('system:news')
    else:
        form = NewsForm()
    return render(request, 'system/news_add.html', {'form': form})

# 新着情報の編集
@login_required
def news_edit(request, pk):
    obj = News.objects.get(id=pk)
    if (request.method == 'POST'):
        form = NewsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(to='/system/news')
    params = {
        'form': NewsForm(instance=obj),
        'id': pk,
    }
    return render(request, 'system/news_edit.html', params)




# 新着情報の削除
def news_delete(request, pk):
    obj = News.objects.get(id=pk)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/system/news')
    params = {
        'obj': obj,
        'id': pk,
    }
    
    return render(request, 'system/news_delete.html', params)