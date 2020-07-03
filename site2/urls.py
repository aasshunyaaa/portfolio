from django.urls import path
from . import views


app_name = 'site2'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/list', views.news_list, name='news_list'),
    path('archive/<int:year>', views.DiaryYearList.as_view(), name='year'),
    path('archive/<int:year>/<int:month>/', views.DiaryMonthList.as_view(), name='month'),
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    # 下記カテゴリによる絞り込みのURL
    path('category/<int:pk>', views.DiaryCategoryList.as_view(), name='category'),

    path('c1', views.c1, name='c1'),
    path('company', views.company, name='company'),
    path('confirm', views.confirm, name='confirm'),
    path('contact', views.contact, name='contact'),
    path('finish', views.finish, name='finish'),
    path('form', views.form, name='form'),
    path('item', views.item, name='item'),
    path('link', views.link, name='link'),
    path('recruit', views.recruit, name='recruit'),
    path('service', views.service, name='service'),
]




