from django.contrib.auth.forms import AuthenticationForm
from site2.models import News
from django import forms
from django_summernote.widgets import SummernoteWidget



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
                'content': SummernoteWidget(),
        }