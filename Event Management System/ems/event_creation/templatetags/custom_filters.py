from django import template
from core.models import EventSsp


register = template.Library()

CATEGORIES = ["Furniture", "Decor", "Stage", "Setup", "Entrance", "Services", "Audio-Visual", "Stalls", "Lighting", "Miscellaneous"]

@register.filter
def dict_key(dictionary, key):
    return dictionary.get(key, None)

@register.filter
def attr(obj, attribute):
    """Get an attribute from an object in the template"""
    return getattr(obj, attribute, None)

@register.filter
def get_next_category(category_name):
    """Returns the next category in the list."""
    try:
        index = CATEGORIES.index(category_name)
        return CATEGORIES[index + 1] if index + 1 < len(CATEGORIES) else category_name
    except ValueError:
        return category_name

@register.filter
def get_previous_category(category_name):
    """Returns the previous category in the list."""
    try:
        index = CATEGORIES.index(category_name)
        return CATEGORIES[index - 1] if index - 1 >= 0 else category_name
    except ValueError:
        return category_name



@register.filter
def multiply(value, arg):
    """
    Multiplies two values.
    Args:
        value: The first value (e.g., quantity).
        arg: The second value (e.g., rate).
    Returns:
        The product of the two values.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0  # Return 0 if there's any error in multiplication
    
@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(key)
    except AttributeError:
        return None
