import re

from locale import normalize

from django.template import loader, TemplateDoesNotExist
from django.template.base import Node, Context, TemplateSyntaxError
from django.utils.encoding import smart_text
from django.utils.translation import get_language, to_locale

try:
    from django.template import Library
except ImportError:
    from django.template.base import Library


register = Library()


# Modified version of kwarg_re from django.template.base that allows us
# to capture kwargs names that contain hyphen in it
kwarg_re = re.compile(r"(?:([\w-]+)=)?(.+)")


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(is_safe=False)
def to_data_string_with_default(value, arg=''):
    """ Given a Python boolean value converts it to string representation so
    we can use it in HTML data attributes. If value is None use given default
    or '' if default is not provided.

    -----       ------
    Value       Output
    -----       ------
    True        "true"
    False       "false"
    None        arg
    """
    if isinstance(value, bool):
        if value:
            return 'true'
        return 'false'

    return value or arg


class SocialWidgetNode(Node):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict((smart_text(k, 'ascii'), v.resolve(context))
                      for k, v in self.kwargs.items())

        # If user didn't specify the language in the template tag arguments get
        # language from Django settings
        if 'language' not in kwargs:
            kwargs.update({'language': get_language()})

        # If user didn't specify the locale in the template tag, guess it from
        # the language
        if 'locale' not in kwargs:
            kwargs.update({'locale': to_locale(kwargs['language'])})

        # Push 'social_widgets_javascript' list into context. We use that list
        # to keep track of loaded external JavaScript files and don't load
        # the same file multiple times in one page when there are multiple
        # widgets from the same social network.
        if 'social_widgets_javascript' not in context.dicts[0]:
            context.dicts[0]['social_widgets_javascript'] = []

        kwargs.update({
            'social_widgets_javascript':
            context.dicts[0]['social_widgets_javascript'][:]
            })

        try:
            template_path = args[0]
        except IndexError:
            return ''

        template = 'social_widgets/%s' % template_path

        # We assume that if there are multiple widget templates in directory
        # (for example in there are 5 templates in "social_widgets/pinterest"
        # directory) then they are all using the same external JavaScript code
        # for loading and initializing.  We want to load this JavaScript code
        # only once when the first widget is rendered, so we use directory name
        # to track if code already had been used. Widget template must also
        # support this feature by checking.
        #
        # {% if not widget_service in social_widgets_javascript #}
        # <!-- Code to load external JavaScript file. -->
        # {% endif %}
        #
        # Alternatively you can disable external JavaScript loading by
        # specifying noscript=True in template tags parameters.
        try:
            widget_service = template_path.split('/')[0]
            kwargs['widget_service'] = widget_service
            if widget_service \
                    not in context.dicts[0]['social_widgets_javascript'] and \
                    not kwargs.get('noscript', False):
                context.dicts[0]['social_widgets_javascript']\
                    .append(widget_service)
        except IndexError:
            pass

        try:
            t = loader.get_template(template)
            return t.render(Context(kwargs))
        except TemplateDoesNotExist:
            return ''


@register.tag
def social_widget_render(parser, token):
    """ Renders the selected social widget. You can specify optional settings
    that will be passed  to widget template.

    Sample usage:
    {% social_widget_render widget_template ke1=val1 key2=val2 %}

    For example to render Twitter follow button you can use code like this:
    {% social_widget_render 'twitter/follow_button.html' username="ev" %}
    """
    bits = token.split_contents()
    tag_name = bits[0]

    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument" %
                                  tag_name)
    args = []
    kwargs = {}

    bits = bits[1:]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to %s tag" %
                                          tag_name)
            name, value = match.groups()

            if name:
                # Replacing hyphens with underscores because
                # variable names cannot contain hyphens.
                name = name.replace('-', '_')
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return SocialWidgetNode(args, kwargs)


@register.assignment_tag
def social_get_facebook_locale(locale):
    """
     Normalize the locale string and split the value needed for the api url
    """
    if locale is None:
        return 'en_US'

    return normalize(locale).split('.')[0]
