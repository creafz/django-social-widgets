=====================
Django Social Widgets
=====================

.. image:: https://pypip.in/download/django-social-widgets/badge.svg
    :target: https://pypi.python.org/pypi/django-social-widgets/
    :alt: Downloads

.. image:: https://readthedocs.org/projects/django-social-widgets/badge/?version=latest
    :target: https://readthedocs.org/projects/django-social-widgets/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/creafz/django-social-widgets.svg?branch=master
    :target: https://travis-ci.org/creafz/django-social-widgets

.. image:: https://coveralls.io/repos/creafz/django-social-widgets/badge.png?branch=master
    :target: https://coveralls.io/r/creafz/django-social-widgets?branch=master

Django app for easy embedding social network widgets and plugins into your site. Supports Facebook, Twitter, Google+, YouTube, Instagram and Pinterest.

Useful links:  `Documentation <https://django-social-widgets.readthedocs.org/en/latest/>`_, `Demo <https://creafz.github.io/django-social-widgets/index.html>`_.

Requirements
------------
* Python 2.6 or 2.7
* Django 1.5 or higher

Quickstart
----------

1. Install from PyPI::

    pip install django-social-widgets

2. Add “social_widgets” to INSTALLED_APPS::

    INSTALLED_APPS = (
     ...
     "social_widgets",
     ...
    )

3. Load the social_widgets template library in every template you want to use it::

      {% load social_widgets %}

4. Place ``{% social_widget_render %}`` code where you want to show the widget. For example if you want to show Facebook Likebox for Facebook Developers page put this code in your template::

    {% social_widget_render 'facebook/likebox.html' href='https://www.facebook.com/FacebookDevelopers' %}


Passing parameters
------------------
Parameter names for widgets are similar to the original parameters with only one change: they use underscore instead of hyphen. So for example if you need to set ``show-screen-name`` parameter for Twitter Follow Button, you should use code like this::

 {% social_widget_render "twitter/follow_button.html" username="BillGates" show_screen_name=True %}

As a value for all parameters you can use a Python value like string, integer or Boolean, for example::

 {% social_widget_render "facebook/likebox.html" app_id=12345678 href="https://www.facebook.com/FacebookDevelopers" show_border=True %}

See this `demo page <https://creafz.github.io/django-social-widgets/index.html>`_ with all supported widgets, their code and available parameters.


Example project
---------------
You can find an example project in "`example_project <https://github.com/creafz/django-social-widgets/tree/master/example_project>`__" directory.


Facebook
--------
* Likebox - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/facebook_widgets.html#likebox>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#facebook-likebox>`__
* Follow Button - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/facebook_widgets.html#follow-button>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#facebook-follow-button>`__
* Embedded Post - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/facebook_widgets.html#embedded-post>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#facebook-embedded-post>`__
* Activity Feed - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/facebook_widgets.html#activity-feed>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#facebook-activity-feed>`__
* Recommendations Feed - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/facebook_widgets.html#recommendations-feed>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#facebook-recommendations-feed>`__

Twitter
-------
* Follow Button - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/twitter_widgets.html#follow-button>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#twitter>`__

Google+
-------
* Person Badge - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/google_widgets.html#google-person-badge>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#google-plus-person-badge>`__
* Page Badge - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/google_widgets.html#google-page-badge>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#google-plus-page-badge>`__
* Community Badge - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/google_widgets.html#google-community-badge>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#google-plus-community-badge>`__

YouTube
-------
* Subscribe Button - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/google_widgets.html#youtube-subscribe-button>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#youtube-subscribe-button>`__

Instagram
---------
* Instagram Badge - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/instagram_widgets.html#instagram-badge>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#instagram-badge>`__

Pinterest
---------
* Follow Button - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/pinterest_widgets.html#follow-button>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#pinterest-follow-button>`__
* Pin Widget - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/pinterest_widgets.html#pin-widget>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#pinterest-pin-widget>`__
* Profile Widget - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/pinterest_widgets.html#profile-widget>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#pinterest-profile-widget>`__
* Board Widget - `Documentation <https://django-social-widgets.readthedocs.org/en/latest/pinterest_widgets.html#board-widget>`__ | `Demo <https://creafz.github.io/django-social-widgets/index.html#pinterest-board-widget>`__
