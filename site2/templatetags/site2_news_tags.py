from django import template
from django.utils import timezone
from site2.models import Category, News

register = template.Library()

@register.inclusion_tag('news_links.html')
def render_news_category():
    return {
        'category_list': Category.objects.all(),
    }