from django import template
from django.utils import timezone
from .models import News

register = template.Library()


@register.inclusion_tag('base_sideber/news_archive.html')
def render_month_links():
    return {
        'dates': News.objects.filter(data__lte=timezone.now()).dates('data', 'month', order='DESC'),
    }