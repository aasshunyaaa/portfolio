from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm, NewsForm
from django.contrib.auth.decorators import login_required
from site2.models import News, Category
from django.contrib import messages
from django.db.models import Q
from . forms import NewsSearchFormSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Login(LoginView):
    form_class = LoginForm
    template_name = 'system/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'system/login.html'


@login_required
def index(request):
    return render(request, 'system/index.html')



# ページネーションの関数
def paginator_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        news_list = paginator.page(1)
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)
    return news_list

# 新着情報の一覧
@login_required
def news(request):
    news = News.objects.all()
    categorys = Category.objects.all()
    formset = NewsSearchFormSet(request.POST or None)
    if request.method == 'POST':
    # 検索機能の処理関数
        formset.is_valid()

        queries = []

        for form in formset:
            q_kwargs = {}
            title = form.cleaned_data.get('title')
            if title:
                q_kwargs['title'] = title
            
            category = form.cleaned_data.get('category')
            if category:
                q_kwargs['category__gte'] = category

            public = form.cleaned_data.get('public')
            if public:
                q_kwargs['public'] = public

            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            news = news.filter(base_query)

    news_list = paginator_query(request, news, 3)
    params = {
        'news': news_list.object_list,
        'news_list': news_list,
        'categorys': categorys,
        'formset': formset,
    }
    return render(request, 'system/news.html', params)




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