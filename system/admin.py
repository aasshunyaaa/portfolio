from django.contrib import admin
from site2.models import News, Category

# from django_summernote.admin import SummernoteModelAdmin

# class NewsAdmin(SummernoteModelAdmin):
    # summernote_fields = '__all__'

admin.site.register(News)
admin.site.register(Category)