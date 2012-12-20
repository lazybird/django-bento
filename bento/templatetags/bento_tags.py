from django import template

from bento.models import TextBox, ImageBox


register = template.Library()


def get_object_or_none(model_class, name):
    """
    Returns the object or None.
    """
    try:
        return model_class.objects.get(name=name)
    except model_class.DoesNotExist:
        return None


@register.inclusion_tag("bento/include-text-box.html", takes_context=True)
def show_text_box(context, name, template='bento/text-box.html'):
    """
    Renders a text box.
    Usage::

        {% show_text_box 'some-name' %}

    You can decide which template to use:

        {% show_text_box 'some-name' 'some-folder/image-box.html' %}
    """
    context.update({
        'box': get_object_or_none(TextBox, name),
        'name': name,
        'template': template,
    })
    return context


@register.inclusion_tag('bento/include-image-box.html', takes_context=True)
def show_image_box(context, name, template='bento/image-box.html'):
    """
    Renders an image box.
    Usage::

        {% show_image_box 'some-name' %}

    You can decide which template to use:

        {% show_image_box 'some-name' 'some-folder/image-box.html' %}

    """
    context.update({
        'box': get_object_or_none(ImageBox, name),
        'name': name,
        'template': template,
    })
    return context
