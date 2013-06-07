from django.conf.urls import patterns, url


urlpatterns = patterns('bento.views',
    url(r'^image-upload/$', 'image_upload', name='bento-image-import'),
    url(r'^text-upload/$', 'text_upload', name='bento-text-import'),
    url(r'^text-edit/(?P<name>[\w-]+)/$', 'text_edit', name='bento-text-edit'),
    url(r'^image-edit/(?P<name>[\w-]+)/$', 'image_edit', name='bento-image-edit'),
)
