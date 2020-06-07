from django.db import models


# 新着情報

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='タイトル') 
    category = models.CharField(max_length=100, verbose_name='カテゴリー')
    content = models.TextField(max_length=500, verbose_name='記事内容')
    data = models.DateTimeField(auto_now_add=True, verbose_name='投稿日')

    def __str__(self):
        return self.title


