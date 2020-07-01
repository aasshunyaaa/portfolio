from django import template
from django.utils import timezone
from site2.models import News

register = template.Library()

@register.inclusion_tag('month_links.html')
def render_month_links():
    return {
        'dates': News.objects.published().dates('data', 'month', order='DESC'),
    }