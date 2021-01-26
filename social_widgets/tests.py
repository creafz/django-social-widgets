from django.template import Template, Context, TemplateSyntaxError
from django.test import TestCase


def render_string(tag_code, context=None):
    # Helper function to render template tags
    t = Template("{% load social_widgets %}" + tag_code)
    return t.render(Context(context or {}))


class BaseTests(TestCase):
    def test_multiple_widgets_with_single_external_javascript(self):
        html = render_string(
            "{% social_widget_render 'facebook/likebox.html' %}"
            "{% social_widget_render 'facebook/follow_button.html' %}"
        )
        self.assertEqual(html.count('facebook-jssdk'), 1)

    def test_language(self):
        html = render_string(
            "{% social_widget_render 'facebook/likebox.html'"
            " language='en-us' %}"
        )
        self.assertIn('en_US', html)


class IncorrectDataTest(TestCase):
    def test_incorrect_template(self):
        html = render_string(
            "{% social_widget_render "
            "'non_existent_dir/non_existent_template.html' %}"
        )
        self.assertEqual(html, "")

    def test_tag_without_parameters(self):
        self.assertRaises(TemplateSyntaxError,
                          render_string, "{% social_widget_render %}")

    def test_malformed_arguments(self):
        self.assertRaises(TemplateSyntaxError,
                          render_string, "{% social_widget_render x==2 %}")

    def test_incorrect_key_value_argument(self):
        self.assertRaises(TemplateSyntaxError,
                          render_string, "{% social_widget_render "
                                         "'facebook/likebox.html' x==2%}")


class TestToDataStringWithDefaultFilter(TestCase):
    def test_true(self):
        html = render_string("{{ True|to_data_string_with_default }}")
        self.assertEqual(html, "true")

    def test_false(self):
        html = render_string("{{ False|to_data_string_with_default }}")
        self.assertEqual(html, "false")

    def test_value(self):
        html = render_string("{{ 'value'|to_data_string_with_default }}")
        self.assertEqual(html, "value")

    def test_blank(self):
        html = render_string("{{ None|to_data_string_with_default }}")
        self.assertEqual(html, "")

    def test_default_arg(self):
        html = render_string(
            "{{ None|to_data_string_with_default:'default' }}"
        )
        self.assertEqual(html, "default")


class TestGetItemFilter(TestCase):
    def test_get_item(self):
        dictionary = {"key": "value"}
        html = render_string("{{ dictionary|get_item:'key' }}",
                             {"dictionary": dictionary})
        self.assertEqual(html, "value")
