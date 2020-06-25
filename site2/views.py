from django.shortcuts import render
from .models import News, Category


# TOPページ
def index(request):
    obj = News.objects.all().order_by('-data')[0:10]
    params = {
        'obj': obj,   
    }
    return render(request, 'site2/index.html', params)

# 新着情報詳細
def news_detail(request, pk):
    obj = News.objects.get(id=pk)
    params = {
        'obj': obj,
    }
    return render(request, 'site2/news_detail.html', params)



def c1(request):
    return render(request, 'site2/c1.html')

def company(request):
    return render(request, 'site2/company.html')

def confirm(request):
    return render(request, 'site2/confirm.html')

def contact(request):
    return render(request, 'site2/contact.html')

def finish(request):
    return render(request, 'site2/finish.html')

def form(request):
    return render(request, 'site2/form.html')

def item(request):
    return render(request, 'site2/item.html')

def link(request):
    return render(request, 'site2/link.html')

def recruit(request):
    return render(request, 'site2/recruit.html')

def service(request):
    return render(request, 'site2/service.html')
