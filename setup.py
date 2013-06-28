import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-gmapify',
    version='0.1',
    author='Javi Imbernon',
    author_email='javi@javimb.com',
    url='https://github.com/javimb/django-gmapify',
    description='Add a Google Map to a template with a simple tag.',
    long_description=README,
    license='BSD',
    packages=['gmapify', 'gmapify.templatetags'],
    package_data={'gmapify': ['templates/gmapify/*']},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
