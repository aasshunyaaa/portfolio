from django import template
from django.utils import timezone
from site2.models import Category, News, Recruit

register = template.Library()

@register.inclusion_tag('recruit_sideber')
def render_news_category():
    return {
        'long_list': Recruit.objects.filter(long_short=False),
        'short_list': Recruit.objects.filter(long_short=True),
    }