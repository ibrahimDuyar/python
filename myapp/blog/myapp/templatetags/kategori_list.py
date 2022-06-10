from myapp.models import KategororiModel
from django import template


register = template.Library()
@register.simple_tag
def kategori_list():

    kategori = KategororiModel.objects.all()

    return kategori
