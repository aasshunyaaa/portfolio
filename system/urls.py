from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('system/login/', views.Login.as_view(), name='login'),
    path('system/logout/', views.Logout.as_view(), name='logout'),
    path('system/index/', views.index, name='index'),
    path('system/news', views.news, name='news'),
    path('system/news/<int:pk>/', views.news_edit, name='news_edit'),
    path('system/news/news_add', views.news_add, name='news_add'),
    path('system/news/<int:pk>', views.news_delete, name='news_delete'),
]
