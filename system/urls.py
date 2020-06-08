from django.urls import path
from . import views

app_name = 'system'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('index/', views.index, name='index'),

]
