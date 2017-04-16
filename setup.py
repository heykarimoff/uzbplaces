import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-uzbplaces',
    install_requires=["django-modeltranslation", "django-geoposition"],
    version='0.4',
    packages=find_packages(exclude=['dist',]),
    package_data={
        'places': ['uzbplaces.fixtures.places.json'],
    },
    include_package_data=True,
    license='MIT License',
    description='UzbPlaces is a simple Django app to integrate places in Uzbekistan.',
    keywords='sample django places development',
    long_description=README,
    url='https://github.com/MrBrownWins/uzbplaces',
    author='Mukhammad Karimov',
    author_email='hey@karimoff.me',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)