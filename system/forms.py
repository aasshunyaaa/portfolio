from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, request,  *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  #←もしかしたら必要ないかも？bootstrapを利用しないため
            field.widget.attrs['placeholder'] = field.label