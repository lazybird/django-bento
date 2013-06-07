
Django Bento
============

    |ZZZZZZZZZZZZZZZZZZZZZZZZZ|
    |:|  +------+ +------+  |:|
    |:|  |      | |      |  |:|
    |:|  |      | |      |  |:| django-bento helps you adding editable
    |:|  |      | |      |  |:| text and image content areas on
    |:|  +------+ +------+  |:| your site. These content boxes are
    |:|  |      | |      |  |:| easy to define in templates and are
    |:|  |      | |      |  |:| updated from Django admin.
    |:|  |      | |      |  |:|
    |:|  +------+ +------+  |:|
    |ZZZZZZZZZZZZZZZZZZZZZZZZZ|



In templates:

    {% load bento_tags %}

    {% show_image_box 'featured-fruit' %}

    {% show_text_box 'about-fruits' %}


In the admin:

![Image Box Admin](https://raw.github.com/lazybird/django-bento/master/docs/images/image-box-admin.png "Image Box Admin")

![Text Box Admin](https://raw.github.com/lazybird/django-bento/master/docs/images/text-box-admin.png "Text Box Admin")


Features
--------

* Dynamic content: Editable from the Django admin
* Edit Link: Admin users see an edit link that bring them to the right
  admin edit page
* Multilingual: Using [django-linguo][linguo] to enable multiple
  languages support for both texts and images
* Export/Import: Backup and restore you content from the admin.
  For instance, you could export from a staging site
  and them import into a live site.


Installation
------------

* Install the package using something like pip and add ``bento`` to
your ``INSTALLED_APPS`` setting.

* Install [django-linguo][linguo] if you need multilingual support.

* Add a URL entry in your projects ``urls.py``.

        urlpatterns = patterns('',
            (r'^boxes/', include('bento.urls')),
        )

* Update the database by running ``syncdb``.


Template Tags
-------------

This is how you define text and an image boxes in templates:

    {% load bento_tags %}

    {% show_image_box 'featured-fruit' %}

    {% show_text_box 'about-fruits' %}


At this point, there is no database entries for these content sections.
If you load the page, you should see some placeholder content.

Custom templates
----------------

You can change the templates by overwriting the defaults files that
 are located here:

* ``templates/bento/text-box.html``
* ``templates/bento/image-box.html``


You can also define the path to your custom templates:


    {% load bento_tags %}

    {% show_image_box 'featured-fruit' template='boxes/custom-text-box.html' %}

    {% show_image_box 'about-fruits' template='boxes/custom-image-box.html' %}



[linguo]: https://github.com/zmathew/django-linguo/
