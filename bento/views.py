from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.views.generic import View

from bento.models import TextBox, ImageBox


class RedirectBoxEdit(RedirectView):

    def get_redirect_url(self, **kwargs):
        name = self.kwargs['name']
        block = self.model_class.objects.get_or_create(name=name)[0]
        return self.get_admin_edit_page(block)

    def get_admin_edit_page(self, instance):
        app_label = instance.__class__._meta.app_label
        model_name = instance.__class__.__name__
        return reverse(
            'admin:%s_%s_change' % (app_label, model_name.lower()),
            args=(instance.pk,)
        )


class RedirectTextBoxEdit(RedirectBoxEdit):
    model_class = TextBox


class RedirectImageBoxEdit(RedirectBoxEdit):
    model_class = ImageBox


class JSONUpload(View):

    def post(self, request, *args, **kwargs):
        json_file = request.FILES['json_file']
        try:
            count = self.deserialize_json(json_file.read())
            messages.success(
                request, 'Successfully processed %s object(s).' % count
            )
        except Exception, e:
            messages.error(request, 'JSON import failed: %s' % e)
        return redirect(self.get_admin_list_page(self.model_class))

    def deserialize_json(self, json_data):
        deserialized = serializers.deserialize('json', json_data)
        count = 0
        for deserialized_item in deserialized:
            count += 1
            try:
                existing_box = self.model_class.objects.get(
                    name=deserialized_item.object.name
                )
                deserialized_item.object.id = existing_box.id
            except self.model_class.DoesNotExist:
                deserialized_item.object.id = None
            deserialized_item.save()
        return count

    def get_admin_list_page(self, model):
        app_label = model._meta.app_label
        model_name = model.__name__
        return reverse('admin:%s_%s_changelist' % (app_label, model_name.lower()))


class TextBoxUpload(JSONUpload):
    model_class = TextBox


class ImageBoxUpload(JSONUpload):
    model_class = ImageBox


text_edit = permission_required('bento.change_textbox', raise_exception=True)(RedirectTextBoxEdit.as_view())
image_edit = permission_required('bento.change_imagebox', raise_exception=True)(RedirectImageBoxEdit.as_view())
text_upload = permission_required('bento.change_textbox', raise_exception=True)(TextBoxUpload.as_view())
image_upload = permission_required('bento.change_imagebox', raise_exception=True)(ImageBoxUpload.as_view())
