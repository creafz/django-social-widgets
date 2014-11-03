import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = PROJECT_ROOT.split(os.sep)[-1]

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
full_path = lambda *parts: os.path.join(PROJECT_ROOT, *parts)
example_path = full_path("..", "..")
if example_path not in sys.path:
    sys.path.append(example_path)

DEBUG = TEMPLATE_DEBUG = True

SECRET_KEY = 'VERY_SECRET_KEY'

STATIC_URL = "/static/"

ROOT_URLCONF = "%s.urls" % PROJECT_DIR

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'social_widgets',
    'example',
)