Twitter Widgets
===============


Follow Button
-------------

* Minimal code::

    {% social_widget_render "twitter/follow_button.html" username="BillGates" %}

* Full code::

    {% social_widget_render "twitter/follow_button.html" username="BillGates" show_screen_name=True show_count=False size="medium" dnt=False %}


**Parameters**

===================== =========================================================================================================================================================== =============
**Parameter**               Description                                                                                                                                                 Default
===================== =========================================================================================================================================================== =============
**Username**              Username to follow (without @)                                                                                                                              None
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**lang**                  Language of the follow button. Available languages: English (en), French (fr), German (de), Italian (it), Spanish (es), Korean (ko) and Japanese (ja).      en
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**width**                 Width of the Follow Button                                                                                                                                  None
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**align**                 Alignment of the Follow Button. Can either be "left" or "right".                                                                                            None
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**show_screen_name**      The user's screen name shows up by default, but you can opt not to show the screen name in the button.                                                      True
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**size**                  The size of the button can render in either "medium", which is the default size, or in "large" - which is the larger button.                                "medium"
--------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
**dnt**                   Enable or disable Do Not Track feature. `More information <https://support.twitter.com/articles/20169421>`_ .                                                False
===================== =========================================================================================================================================================== =============

* Demo: https://creafz.github.io/django-social-widgets/index.html#twitter

* Twitter documentation: https://dev.twitter.com/web/follow-button