from django import template

from core import models


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_homepage(context):
    site = context['request'].site
    return models.HomePage.objects.filter(id=site.root_page_id).first()
