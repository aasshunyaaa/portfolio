from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
      form = News
      fields = ('title', 'category', 'content', 'data') 