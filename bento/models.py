from django.db import models
from django.utils.translation import ugettext_lazy as _


# By default Django prevents you from adding custom attributes to the
# Meta class. Let's allow the 'translate' option to be defined even
# tough it's only needed when django-linguo is available.
models.options.DEFAULT_NAMES += ('translate',)

try:
    from linguo.managers import MultilingualManager as BoxManager
    from linguo.models import MultilingualModel as BoxModel
except ImportError:
    from django.db.models import Model as BoxModel
    from django.db.models import Manager as BoxManager


class TextBox(BoxModel):
    name = models.SlugField(_('name'), max_length=255, unique=True)
    text = models.TextField(_('text'), blank=True)
    modification_date = models.DateTimeField(_('modification date'),
        auto_now=True)

    objects = BoxManager()

    class Meta:
        verbose_name = _("Text Box")
        verbose_name_plural = _("Text Boxes")
        translate = ('text',)

    def __unicode__(self):
        return self.name


class ImageBox(BoxModel):
    name = models.SlugField(_('name'), max_length=255, unique=True)
    image = models.ImageField(_('image'), upload_to='bento/images')
    modification_date = models.DateTimeField(_('modification date'),
        auto_now=True)
    alternate_text = models.CharField(_('alternate text'), max_length=255,
        blank=True)
    link = models.CharField(_('link'), max_length=255, blank=True,
        help_text=_('http://external.site.com/ or /relative/link/'))

    objects = BoxManager()

    class Meta:
        verbose_name = _('Image Box')
        verbose_name_plural = _('Image Boxes')
        translate = ('image', 'alternate_text', 'link')

    def __unicode__(self):
        return self.name
