import datetime

from django.contrib import admin
from django.core import serializers
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from bento.models import TextBox, ImageBox


class TextBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'modification_date')
    actions = ['export_selected_objects']

    def export_selected_objects(self, request, queryset):
        response = HttpResponse(mimetype='application/json')
        filename = '%(model)s-%(date)s.json' % {
            'model': self.opts.module_name,
            'date': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
        }
        response['Content-Disposition'] = u'attachment; filename=%s' % filename
        serializers.serialize('json', queryset, stream=response)
        return response
    export_selected_objects.short_description = 'Export to JSON'


class ImageBoxAdmin(TextBoxAdmin):
    list_display = ('name', 'preview', 'modification_date')

    def preview(self, obj):
        template = u"""<img src="{url}" style="max-height: 48px;" />"""
        url = obj.image.url if obj.image else ''
        return template.format(url=url)
    preview.short_description=_('preview')
    preview.allow_tags = True


admin.site.register(TextBox, TextBoxAdmin)
admin.site.register(ImageBox, ImageBoxAdmin)
