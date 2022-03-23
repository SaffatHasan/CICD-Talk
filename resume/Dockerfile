FROM python:3.8-slim

WORKDIR /data

RUN pip install Jinja2 PyYaml

ENTRYPOINT python resume/render_resume_template.py
