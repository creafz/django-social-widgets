=====================
Django Social Widgets
=====================

Django app for easy embedding social network widgets and plugins into your site. Supports Facebook, Twitter, Google+, YouTube, Instagram and Pinterest. Demo: 
`https://creafz.github.io/django-social-widgets/index.html <https://creafz.github.io/django-social-widgets/index.html>`_.

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

Supported Widgets
-----------------

Facebook
--------
* `Likebox <https://creafz.github.io/django-social-widgets/index.html#facebook-likebox>`_
* `Follow Button <https://creafz.github.io/django-social-widgets/index.html#facebook-follow-button>`__
* `Embedded Post <https://creafz.github.io/django-social-widgets/index.html#facebook-embedded-post>`_
* `Activity Feed <https://creafz.github.io/django-social-widgets/index.html#facebook-activity-feed>`_
* `Recommendations Feed <https://creafz.github.io/django-social-widgets/index.html#facebook-recommendations-feed>`_

Twitter
-------
* `Follow Button <https://creafz.github.io/django-social-widgets/index.html#twitter>`__

Google+
-------
* `Person Badge <https://creafz.github.io/django-social-widgets/index.html#google-plus-person-badge>`_
* `Page Badge <https://creafz.github.io/django-social-widgets/index.html#google-plus-page-badge>`_
* `Community Badge <https://creafz.github.io/django-social-widgets/index.html#google-plus-community-badge>`_

YouTube
-------
* `Subscribe Button <https://creafz.github.io/django-social-widgets/index.html#youtube-subscribe-button>`_

Instagram
---------
* `Instagram Badge <https://creafz.github.io/django-social-widgets/index.html#instagram-badge>`_

Pinterest
---------
* `Follow Button <https://creafz.github.io/django-social-widgets/index.html#pinterest-follow-button>`__
* `Pin Widget <https://creafz.github.io/django-social-widgets/index.html#pinterest-pin-widget>`_
* `Profile Widget <https://creafz.github.io/django-social-widgets/index.html#pinterest-profile-widget>`_
* `Board Widget <https://creafz.github.io/django-social-widgets/index.html#pinterest-board-widget>`_

