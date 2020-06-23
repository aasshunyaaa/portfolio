from django.contrib.auth.forms import AuthenticationForm
from site2.models import News
from django import forms
from django_summernote.widgets import SummernoteWidget
from site2.models import Category, PUBLIC_CHOICES, News, Recruit
from site2 import models



class LoginForm(AuthenticationForm):
    def __init__(self, request,  *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  
            field.widget.attrs['placeholder'] = field.label


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'category', 'content',)
        widgets = {
            'category' :forms.CheckboxSelectMultiple,
            
        }

PUBLIC_CHOICES = PUBLIC_CHOICES + [('', '選択してください')]
class NewsSearchForm(forms.Form):
    title = forms.CharField(max_length='100', required=False)
    category = forms.ModelChoiceField(models.Category.objects, label='カテゴリー', required=True)
    public = forms.ChoiceField(label='公開/非公開', choices=PUBLIC_CHOICES, required=False)


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ('title', 'discription', 'public_status', 'long_short')




    

