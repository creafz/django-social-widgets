Google+ and YouTube Widgets
===========================


Google+ Person Badge
--------------------

* Minimal code::

    {% social_widget_render "google/plus_person_badge.html" href="https://plus.google.com/+SergeyBrin" %}

* Full code::

    {% social_widget_render "google/plus_person_badge.html" language="en-US" href="https://plus.google.com/+SergeyBrin" layout="portrait" showcoverphoto=True showtagline=True theme="light" width=300 %}


**Parameters**

=================== ================================================================================================================================================ ===============
**Parameter**           Description                                                                                                                                      Default
=================== ================================================================================================================================================ ===============
**language**            Language of the Google+ badge                                                                                                                    "en-US"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**href**                URL to the Google+ page                                                                                                                          None
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**layout**              Sets the orientation of the badge. Can either be "landscape" or "portrait".                                                                      "portrait"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showcoverphoto**      Displays the cover photo in the badge if set to true and the photo exists                                                                        True
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showtagline**         Displays the user's tag line if set to true.                                                                                                     True
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**theme**               The color theme of the badge. Use dark when placing the badge on a page with a dark background.                                                  "light"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**width**               The pixel width of the badge to render. The following ranges are valid: Portrait layout (180-450 pixels), Landscape layout (273-450 pixels)      300
=================== ================================================================================================================================================ ===============

* Demo: https://creafz.github.io/django-social-widgets/index.html#google-plus-person-badge

* Google documentation: https://developers.google.com/+/web/badge/#person-badge


Google+ Page Badge
------------------

* Minimal code::

    {% social_widget_render "google/plus_page_badge.html" href="https://plus.google.com/110967630299632321627" %}

* Full code::

    {% social_widget_render "google/plus_page_badge.html" language="en-US" href="https://plus.google.com/110967630299632321627" layout="portrait" showcoverphoto=True showtagline=True theme="light" width=300 %}


**Parameters**

=================== ================================================================================================================================================ ===============
**Parameter**           Description                                                                                                                                      Default
=================== ================================================================================================================================================ ===============
**language**            Language of the Google+ badge                                                                                                                    "en-US"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**href**                URL to the Google+ page                                                                                                                          None
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**layout**              Sets the orientation of the badge. Can either be "landscape" or "portrait".                                                                      "portrait"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showcoverphoto**      Displays the cover photo in the badge if set to true and the photo exists                                                                        True
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showtagline**         Displays the user's tag line if set to true.                                                                                                     True
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**theme**               The color theme of the badge. Use dark when placing the badge on a page with a dark background.                                                  "light"
------------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**width**               The pixel width of the badge to render. The following ranges are valid: Portrait layout (180-450 pixels), Landscape layout (273-450 pixels)      300
=================== ================================================================================================================================================ ===============

* Demo: https://creafz.github.io/django-social-widgets/index.html#google-plus-page-badge

* Google documentation: https://developers.google.com/+/web/badge/#page-badge


Google+ Community Badge
-----------------------

* Minimal code::

    {% social_widget_render "google/plus_community_badge.html" href="https://plus.google.com/communities/113527920160449995981" %}

* Full code::

   {% social_widget_render "google/plus_community_badge.html" language="en-US" href="https://plus.google.com/communities/113527920160449995981" layout="portrait" showphoto=True showowners=False showtagline=True theme="light" width=300 %}


**Parameters**

================ ================================================================================================================================================ ===============
**Parameter**        Description                                                                                                                                      Default
================ ================================================================================================================================================ ===============
**language**         Language of the Google+ badge                                                                                                                    "en-US"
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**href**             URL to the Google+ page                                                                                                                          None
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**layout**           Sets the orientation of the badge. Can either be "landscape" or "portrait".                                                                      "portrait"
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showphoto**        Displays the community profile photo if set to true and the photo exists.                                                                        True
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showowners**       Displays a list of community owners if set to true.                                                                                              False
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**showtagline**      Displays the user's tag line if set to true.                                                                                                     True
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**theme**            The color theme of the badge. Use dark when placing the badge on a page with a dark background.                                                  "light"
---------------- ------------------------------------------------------------------------------------------------------------------------------------------------ ---------------
**width**            The pixel width of the badge to render. The following ranges are valid: Portrait layout (180-450 pixels), Landscape layout (273-450 pixels)      300
================ ================================================================================================================================================ ===============

* Demo: https://creafz.github.io/django-social-widgets/index.html#google-plus-community-badge

* Google documentation: https://developers.google.com/+/web/badge/#community-badge


YouTube Subscribe Button
------------------------

* Minimal code::

    {% social_widget_render "google/youtube_subscribe_button.html" channel="GoogleDevelopers" %}

* Full code::

    {% social_widget_render "google/youtube_subscribe_button.html" channel="GoogleDevelopers" theme="default" layout="default" count="default" %}


**Parameters**

============== ============================================================================================================================== ==============
**Parameter**      Description                                                                                                                    Default
============== ============================================================================================================================== ==============
**language**       Language of the button                                                                                                         "en-US"
-------------- ------------------------------------------------------------------------------------------------------------------------------ --------------
**channel**        The name of the channel associated with the button                                                                             None
-------------- ------------------------------------------------------------------------------------------------------------------------------ --------------
**layout**         The format for the button. Can either be "default" or "full"                                                                   "default"
-------------- ------------------------------------------------------------------------------------------------------------------------------ --------------
**theme**          Specifies the color scheme to use for the button. Can either be "default" or "dark"                                            "default"
-------------- ------------------------------------------------------------------------------------------------------------------------------ --------------
**count**          Indicates whether the button displays the number of subscribers that the channel has. Can either be "default" or "count".      "default"
============== ============================================================================================================================== ==============

* Demo: https://creafz.github.io/django-social-widgets/index.html#youtube-subscribe-button

* Google documentation: https://developers.google.com/youtube/youtube_subscribe_button