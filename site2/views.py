from django.shortcuts import render
from .models import News, Category
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
class DiaryYearList(ArchiveListMixin, generic.YearArchiveView):

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年の記事'.format(self.kwargs['year'])
        return context

# 月別アーカイブ
class DiaryMonthList(ArchiveListMixin, generic.MonthArchiveView):
    month_format = '%m'

    def get_queryset(self):
        return super().get_queryset().select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = '{}年{}月の記事'.format(self.kwargs['year'], self.kwargs['month'])
        return context


# 新着カテゴリ別ソート機能
class DiaryCategoryList(ArchiveListMixin, generic.ArchiveIndexView):

    def get_queryset(self):
        self.category = category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category).select_related('category')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = News.objects.filter()
        return context
    





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

def recruit(request):
    return render(request, 'site2/recruit.html')

def service(request):
    return render(request, 'site2/service.html')
