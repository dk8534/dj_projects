from django import template 
register=template.Library() 
@register.filter(name='f4upper') 
def first_eight_upper(value): 
    '''''This is my own filter''' 
    result=value[:4].upper() 
    return result 