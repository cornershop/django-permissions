import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__),
                           'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-permissions',
    version='0.1.1',
    packages=['django_permissions', 'django_permissions.migrations', 'django_permissions.tests'],
    include_package_data=True,
    license='BSD License',
    description='Parametrized Role Based Access Control (PRBAC) system',
    long_description=README,
    url='',
    author='Richard Barrios',
    author_email='richard@cornershoapp.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)