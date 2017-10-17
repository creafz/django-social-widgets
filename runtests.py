#!/usr/bin/env python
import sys
import os

from django.conf import settings
from django.core.management import call_command

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


settings.configure(
    INSTALLED_APPS=('social_widgets',),
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:',
        }
    },
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(os.path.dirname(__file__), 'social_widgets/templates')],
            #'APP_DIRS': True,
        },
    ]
)

# Added to support Django >= 1.7
import django
if django.VERSION[:2] >= (1, 7):
    django.setup()

if __name__ == "__main__":
    call_command('test', 'social_widgets')
