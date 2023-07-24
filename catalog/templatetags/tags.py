from django import template

register = template.Library()


@register.filter()
def media_path(path_to_image):
    if path_to_image:
        return f"/media/{path_to_image}"
    return "#"


@register.simple_tag()
def mediapath(path_to_image):
    if path_to_image:
        return f"/media/{path_to_image}"
    return "#"
