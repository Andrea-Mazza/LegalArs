from django import template
import json
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name='get_attribute')
def get_attribute(obj, attr):
    return obj.__getattribute__(attr)


@register.filter(is_safe=True)
def json_loads(value):
    try:
        return json.loads(value)
    except (TypeError, ValueError, KeyError):
        return {}


@register.filter(is_safe=True)
def to_json(value):
    return mark_safe(json.dumps(value))
