# django-static-version
A simple Django template tag to automatically version static files.

## Usage
Simply add the code in `static_version.py` into one of your template tag files. For more information on how to write custom template tags, see https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/.

Then, simply use the `static_version` template tag in place of the default `static` template tag. For example, if you had included the `static_version` template tag in `templatetags/custom_tags.py` and wanted to include a CSS file:

```
{% load custom_tags %}
...
<link rel="stylesheet" type="text/css" href="{% static_version 'admin/css/base.css' %}" />
```
