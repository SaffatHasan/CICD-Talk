""" render_resume_template.py - Perform variable substitutions on a LaTeX template
"""

import os
import jinja2
import yaml


def generate_resume(template_file, data_file, output_file):
    """ fetch template and render to file
    """
    template = get_template(template_file)
    data = get_data(data_file)
    render_template_to_file(template, data, output_file)


def get_template(template_file):
    """ Defines the jinja Environment and returns template string

    ARGS:
        template_file(string): name of the file which contains the latex template

    RETURNS:
        Jinja2 template
    """
    latex_jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'),
        block_start_string=r'\BLOCK{',
        block_end_string='}',
        variable_start_string=r'\VAR{',
        variable_end_string='}',
        comment_start_string=r'\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
    )

    with open(template_file, encoding='UTF-8') as file_handle:
        contents = file_handle.read()

    return latex_jinja_env.from_string(contents)


def render_template_to_file(template, data, output_file):
    """ Takes a template and path and outputs the rendered resume

    ARGS:
        template(Jinja2.Template): template to be rendered to
        data(yaml.Yaml): personal data to render into the resume template
        output_file(string): destination, specified as dist/{resume_name}.pdf
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding='UTF-8') as file_handle:
        file_handle.write(template.render(data))


def get_data(data_file):
    """ Returns the dictionary representation of the `resources/data.yml` file

    RETURNS:
        key/value pairs of data
    """
    with open(data_file, 'r', encoding='UTF-8') as stream:
        data = yaml.safe_load(stream)
    return data


if __name__ == "__main__":
    generate_resume(
        template_file="src/resume.tex",
        data_file="src/data.yml",
        output_file="dist/resume.tex",
    )
