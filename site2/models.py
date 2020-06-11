from django.db import models
from mdeditor.fields import MDTextField


# 新着情報

class Category(models.Model):
    name = models.CharField(max_length=100,)
    def __str__(self):
        return self.name
    

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル') 
    category = models.ManyToManyField(Category, verbose_name='カテゴリー')
    content = MDTextField(max_length=500, verbose_name='記事内容')
    data = models.DateTimeField(auto_now_add=True, verbose_name='投稿日')

    def __str__(self):
        return self.title


