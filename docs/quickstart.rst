Quickstart
==========

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

4. Place ``{% social_widget_render %}`` code where you want to show the widget.
   For example if you want to show Facebook Likebox for Facebook Developers
   page put this code in your template::

    {% social_widget_render 'facebook/likebox.html' href='https://www.facebook.com/FacebookDevelopers' %}

