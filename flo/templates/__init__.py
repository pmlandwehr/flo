import os

import jinja2

from ..exceptions import JinjaError


def render_from_string(template_string, **context_dict):
    env = jinja2.Environment()
    try:
        template_obj = env.from_string(template_string)
    except jinja2.exceptions.TemplateSyntaxError, error:
        raise JinjaError(error)
    return template_obj.render(**context_dict)


def render_from_file(template_file, **context_dict):
    this_directory = os.path.dirname(os.path.abspath(__file__))
    loader = jinja2.FileSystemLoader(this_directory)
    env = jinja2.Environment(loader=loader)
    template_obj = env.get_template(template_file)
    return template_obj.render(**context_dict)
