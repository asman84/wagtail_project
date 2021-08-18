from django import template

register = template.Library()




@register.simple_tag(takes_context=True)
def var_exists(context):
    dicts = context.dicts  # array of dicts
    if dicts:
        return dicts
    return False