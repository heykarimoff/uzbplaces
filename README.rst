=====
UzbPlaces
=====


[![Documentation Status](https://readthedocs.org/projects/uzbplaces/badge/?version=latest)](http://uzbplaces.readthedocs.io/en/latest/?badge=latest)


UzbPlaces is a simple Django app to integrate places in Uzbekistan. For each
province, there are regions.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "uzbplaces" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'uzbplaces',
    ]
2. Add GEOPOSITION_GOOGLE_MAPS_API_KEY to your settings.py

3. Add following to settings.py
    # Model Translation
    MODELTRANSLATION_LANGUAGES = ('en', 'ru', 'uz')
    MODELTRANSLATION_ADMIN_SCRIPTS = (
        'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )

    MODELTRANSLATION_ADMIN_STYLE = {
        'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }

4. Include the polls URLconf in your project urls.py like this::

    url(r'^uzbplaces/', include('uzbplaces.urls')),

5. Run `python manage.py migrate` to create the polls models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/uzbplaces/ to use.
