Usage
=====

Passing parameters
------------------

Parameter names for widgets are similar to the original parameters with only one change: they use underscore instead of hyphen. So for example if you need to set ``show-screen-name`` parameter for Twitter Follow Button, you should use code like this::

    {% social_widget_render "twitter/follow_button.html" username="BillGates" show_screen_name=True %}

As a value for all parameters you can use a Python value like string, integer or Boolean, for example::

    {% social_widget_render "facebook/likebox.html" app_id=12345678 href="https://www.facebook.com/FacebookDevelopers" show_border=True %}


JavaScript initialization code
------------------------------

All widgets (except Instagram badge) require JavaScript code to be loaded and executed before widget is rendered.
django-social-widgets tracks and loads this code only once for each social network,
so for example if you have 3 facebook widgets on one page, the Facebook JavaScript
code will be loaded only once (when first widget is being rendered). If you already
have this JavaScript code on the page (for example you have already loaded Facebook
JavaScript SDK to use it with your own scripts) you can tell the django-social-widgets
not to load it again. To do this, add ``noscript=True parameter`` to the
``{% social_widget_render %}`` tag, for example::

    {% social_widget_render 'facebook/likebox.html' noscript=True href='https://www.facebook.com/FacebookDevelopers' %}

If you have multiple widgets on one page and you want to disable JavaScript
loading for all of them you should add the ``noscript=True`` parameter to
each call of ``{% social_widget_render %}``.



