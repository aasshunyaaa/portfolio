from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('system/login/', views.Login.as_view(), name='login'),
    path('system/logout/', views.Logout.as_view(), name='logout'),
    path('system/index/', views.index, name='index'),
    # 以下新着情報
    path('system/news/', views.news, name='news'),
    path('system/news/<int:pk>/', views.news_edit, name='news_edit'),
    path('system/news/news_add', views.news_add, name='news_add'),
    path('system/news/<int:pk>', views.news_delete, name='news_delete'),
    # 以下採用ページ
    path('system/recruit/', views.recruit, name='recruit'),
    path('system/recruit/add/', views.recruit_add, name='recruit_add'),
    path('system/recruit/<int:pk>', views.recruit_edit, name='recruit_edit'),
    path('system/recruit/del/<int:pk>', views.recruit_delete, name='recruit_delete'),
]
