=====
UzbPlaces
=====

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

2. Include the polls URLconf in your project urls.py like this::

    url(r'^uzbplaces/', include('uzbplaces.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/uzbplaces/ to use.
