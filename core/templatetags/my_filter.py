from django import template
from core.models import Product

register=template.Library()

@register.simple_tag
def get_product(offset,limit,order_by):
    if order_by==0:
        return Product.objects.filter(active=True).order_by('-update_at')[offset:limit]
    return Product.objects.filter(active=True).order_by('update_at')[offset:limit]

@register.filter
def get_lower(values):
    return values.upper()