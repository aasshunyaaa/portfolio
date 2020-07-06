from django.shortcuts import render
from .models import News, Category, Recruit
from system.views import paginator_query
from django.shortcuts import get_object_or_404
from django.views import generic



# TOPページ
def index(request):
    obj = News.objects.all().order_by('-data')[0:10]
    params = {
        'obj': obj,   
        'title': 'ポートフォリオTOP',
    }
    return render(request, 'site2/index.html', params)


   # 新着情報一覧
def news_list(request):
    obj = News.objects.all().order_by('-data')
    news_list = paginator_query(request, obj, 10)

    params = {
        'obj': news_list,
        'paginator_list': news_list,
        'title': '新着情報一覧',
        'daytime': '2019',
    }

    return render(request, 'site2/news_list.html', params)

class ArchiveListMixin:
    model = News
    date_field = 'data'
    allow_empty = True
    make_object_list = True
    template_name = 'site2/archive_category.html'






# 年別アーカイブ
def news_year_list(request, year):
    obj = News.objects.filter(data__year=year).order_by('-data')
    obj_list = paginator_query(request, obj, 6)
    daytime = '{}年の記事'.format(year)

    params = {
        'obj': obj_list.object_list,
        'daytime': daytime,
        'paginator_list' :obj_list
    }
    return render(request, 'site2/archive_category.html', params)


# 月別アーカイブ
def news_month_list(request, year, month):
    obj = News.objects.filter(data__month=month).order_by('-data')
    daytime = '{}年{}月の記事'.format(year, month)
    obj_list = paginator_query(request, obj, 6)
    params = {
        'obj': obj_list.object_list,
        'daytime': daytime,
        'paginator_list': obj_list,
    }

    return render(request, 'site2/archive_category.html', params)


# 新着カテゴリ別ソート機能
def news_category_list(request, pk):
    obj = News.objects.filter(category=pk).order_by('-data')
    category_name = Category.objects.get(id=pk)
    obj_list = paginator_query(request, obj, 6)
    daytime = '【{}】の記事一覧'.format(category_name)
    params = {
        'obj': obj_list.object_list,
        'daytime': daytime,
        'paginator_list': obj_list,
    }
    return render(request, 'site2/archive_category.html', params)


# 新着情報詳細
def news_detail(request, pk):
    obj = News.objects.get(id=pk)
    params = {
        'obj': obj,
        'title': '新着情報詳細',
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


# 採用ページ関数
def recruit(request):
    obj_short = Recruit.objects.filter(long_short=True, public_status=True)[:5]
    obj_long = Recruit.objects.filter(long_short=False, public_status=True)[:5]
    params = {
        'obj_short': obj_short,
        'obj_long': obj_long,
        
    }
    return render(request, 'site2/recruit.html', params)

# 採用ページ長期アーカイブ
def recruit_archive_long(request):
    obj_recruit = Recruit.objects.filter(long_short=False)

    params = {
        'title': '長期',
        'obj_recruit': obj_recruit,
    }

    return render(request, 'site2/archive_recruit.html', params)

# 採用ページ短期アーカイブ
def recruit_archive_short(request):
    obj_recruit = Recruit.objects.filter(long_short=True)

    params = {
        'title': '短期',
        'obj_recruit': obj_recruit,
    }

    return render(request, 'site2/archive_recruit.html', params)


def service(request):
    return render(request, 'site2/service.html')
