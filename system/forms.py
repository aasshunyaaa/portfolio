from django.contrib.auth.forms import AuthenticationForm
from site2.models import News
from django import forms



class LoginForm(AuthenticationForm):
    def __init__(self, request,  *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  
            field.widget.attrs['placeholder'] = field.label


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'category', 'content', 'data')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        CHOICE = ('お知らせ', '採用について', '製品情報', '株主の皆様へ')
        self.fields['category'].choice=CHOICE
