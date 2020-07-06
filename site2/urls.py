from django.urls import path
from . import views


app_name = 'site2'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/list', views.news_list, name='news_list'),
    # 下記日時による絞り込み
    path('archive/<int:year>', views.news_year_list, name='year'),
    path('archive/<int:year>/<int:month>/', views.news_month_list, name='month'),
    # 下記記事詳細
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    # 下記カテゴリによる絞り込みの
    path('category/<int:pk>', views.news_category_list, name='category'),
    path('c1', views.c1, name='c1'),
    path('company', views.company, name='company'),
    path('confirm', views.confirm, name='confirm'),
    path('contact', views.contact, name='contact'),
    path('finish', views.finish, name='finish'),
    path('form', views.form, name='form'),
    path('item', views.item, name='item'),
    path('link', views.link, name='link'),
    path('recruit', views.recruit, name='recruit'),
    # 採用アーカイブ
    path('recruit/long', views.recruit_archive_long, name='recruit_long'),
    path('recruit/short', views.recruit_archive_short, name='recruit_short'),
    path('service', views.service, name='service'),
]




