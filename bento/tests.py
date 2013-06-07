from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.test import TestCase

from bento.models import TextBox, ImageBox


IMPORT_JSON_DATA = """
    [
        {
            "pk": 1,
            "model": "bento.textbox",
            "fields": {
                "name": "json-upload-text",
                "text": "Some Text",
                "modification_date": "2011-01-01 00:00:00"
            }
        }
    ]
"""


class BentoTestHelper(object):

    def login_as_admin(self):
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='email@test.com'
        )
        self.client.login(username='admin', password='admin')


class TextBoxTests(BentoTestHelper, TestCase):

    def setUp(self):
        self.login_as_admin()
        self.box = TextBox.objects.create(name='some-text-box')
        self.edit_url = reverse('bento-text-edit', args=['some-text-box'])
        self.import_url = reverse('bento-text-import')

    def test_edit_link_redirects_to_admin(self):
        response = self.client.get(self.edit_url)
        expected_url = reverse('admin:bento_textbox_change', args=[self.box.pk])
        self.assertRedirects(response, expected_url, status_code=301)

    def test_edit_link_creates_a_new_text_box(self):
        count_before = TextBox.objects.count()
        url = reverse('bento-text-edit', args=['new-text-box'])
        self.client.get(url)
        count_after = TextBox.objects.count()
        self.assertEqual(count_after, count_before + 1)

    def test_json_import_adds_new_text_box(self):
        json_file = SimpleUploadedFile('text-box.json', IMPORT_JSON_DATA)
        count_before = TextBox.objects.count()
        post_data = {'json_file': json_file}
        self.client.post(self.import_url, post_data)
        count_after = TextBox.objects.count()
        self.assertEqual(count_after, count_before + 1)

    def test_invalid_json_displays_error(self):
        json_file = SimpleUploadedFile('text-box.json', 'invalid-json')
        post_data = {'json_file': json_file}
        response = self.client.post(self.import_url, post_data, follow=True)
        self.assertContains(response, 'JSON import failed')


class ImageBoxTests(BentoTestHelper, TestCase):

    def setUp(self):
        self.login_as_admin()
        self.box = ImageBox.objects.create(name='some-image-box')
        self.edit_url = reverse('bento-image-edit', args=['some-image-box'])

    def test_edit_link_redirects_to_admin(self):
        response = self.client.get(self.edit_url)
        expected_url = reverse('admin:bento_imagebox_change', args=[self.box.pk])
        self.assertRedirects(response, expected_url, status_code=301)

    def test_edit_link_creates_a_new_image_box(self):
        count_before = ImageBox.objects.count()
        url = reverse('bento-image-edit', args=['new-image-box'])
        self.client.get(url)
        count_after = ImageBox.objects.count()
        self.assertEqual(count_after, count_before + 1)
