from django.db import models
from mdeditor.fields import MDTextField


# 新着情報

class Category(models.Model):
    name = models.CharField(max_length=100,)
    def __str__(self):
        return self.name
    
PUBLIC_CHOICES = [
    ('1', '公開'),
    ('2', '非公開'),
]

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル') 
    category = models.ManyToManyField(Category, verbose_name='カテゴリー')
    content = MDTextField(max_length=500, verbose_name='記事内容')
    public_status = models.BooleanField(verbose_name='公開/非公開', default=True, choices=PUBLIC_CHOICES)
    data = models.DateTimeField(auto_now_add=True, verbose_name='投稿日')

    def __str__(self):
        return self.title


class Recruit(models.Model):
    title = models.CharField('タイトル', max_length=100)
    discription = MDTextField(max_length=500, verbose_name='記事内容')
    public_status = models.BooleanField('チェックで公開')
    long_short = models.BooleanField('チェックで短期', default=False)

    def __str__(self):
        return self.title



    
