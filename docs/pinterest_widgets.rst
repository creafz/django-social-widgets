Pinterest Widgets
=================


Follow Button
-------------

* Full code::

    {% social_widget_render "pinterest/follow_button.html" href="http://www.pinterest.com/pinterest/" fullname="Pinterest" %}

**Parameters**

============== =================================================== ============
**Parameter**      Description                                         Default
============== =================================================== ============
**href**           Pinterest User URL                                  None
-------------- --------------------------------------------------- ------------
**fullname**       User fullname that will be shown on the button      None
============== =================================================== ============

* Demo: https://creafz.github.io/django-social-widgets/index.html#pinterest-follow-button

* Pinterest documentation: https://business.pinterest.com/en/widget-builder#do_follow_me_button


Pin Widget
----------

* Full code::

    {% social_widget_render "pinterest/pin_widget.html" href="http://www.pinterest.com/pin/99360735500167749/" %}

**Parameters**

============== ====================== ============
**Parameter**      Description            Default
============== ====================== ============
**href**           Pinterest Pin URL      None
============== ====================== ============

* Demo: https://creafz.github.io/django-social-widgets/index.html#pinterest-pin-widget

* Pinterest documentation: https://business.pinterest.com/en/widget-builder#do_embed_pin


Profile Widget
--------------

* Minimal code::

    {% social_widget_render "pinterest/profile_widget.html" href="http://www.pinterest.com/pinterest/" %}

* Full code::

    {% social_widget_render "pinterest/profile_widget.html" href="http://www.pinterest.com/pinterest/" pin_scale_width=80 pin_scale_height=320 pin_board_width=400 %}

**Parameters**

===================== ========================== ============
**Parameter**             Description                Default
===================== ========================== ============
**href**                  Pinterest User URL         None
--------------------- -------------------------- ------------
**pin_scale_width**       Width of a single pin      80
--------------------- -------------------------- ------------
**pin_scale_height**      Height of a singe pin      320
--------------------- -------------------------- ------------
**pin_board_width**       Width of the widget        400
===================== ========================== ============

* Demo: https://creafz.github.io/django-social-widgets/index.html#pinterest-profile-widget

* Pinterest documentation: https://business.pinterest.com/en/widget-builder#do_embed_user


Board Widget
------------

* Minimal code::

    {% social_widget_render "pinterest/board_widget.html" href="http://www.pinterest.com/pinterest/pin-pets/" %}

* Full code::

    {% social_widget_render "pinterest/board_widget.html" href="http://www.pinterest.com/pinterest/pin-pets/" pin_scale_width=80 pin_scale_height=320 pin_board_width=400 %}

**Parameters**

===================== ========================== ============
**Parameter**             Description                Default
===================== ========================== ============
**href**                  Pinterest User URL         None
--------------------- -------------------------- ------------
**pin_scale_width**       Width of a single pin      80
--------------------- -------------------------- ------------
**pin_scale_height**      Height of a singe pin      320
--------------------- -------------------------- ------------
**pin_board_width**       Width of the widget        400
===================== ========================== ============

* Demo: https://creafz.github.io/django-social-widgets/index.html#pinterest-board-widget

* Pinterest documentation: https://business.pinterest.com/en/widget-builder#do_embed_board