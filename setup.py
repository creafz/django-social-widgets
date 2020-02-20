import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-social-widgets',
    version='0.4.1',
    packages=['social_widgets'],
    include_package_data=True,
    license='MIT License',
    description='Django app for easy embedding social network widgets and '
                'plugins into your site. Supports Facebook, Twitter, Google+, '
                'YouTube, Instagram and Pinterest.',
    long_description=README,
    keywords='Django, social network, template, facebook, twitter',
    url='https://github.com/creafz/django-social-widgets',
    download_url=
    'https://github.com/creafz/django-social-widgets/tarball/0.4.0',
    author='Alex Parinov',
    author_email='creafz@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=["django>=1.5"],
)
