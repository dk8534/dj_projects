from django import template
register = template.Library()

# coustomize filter
@register.filter(name='ffcu')
def first_four_character_in_upper(value):
    result = value[:4].upper()
    return result