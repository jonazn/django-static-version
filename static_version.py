from django import template
from django.templatetags.static import static
from django.conf import settings
import os

register = template.Library()
    
# pass the static file path + name and return the last modified date
# used for static file versioning (append to end of URL: 'style.css?v=010115')
@register.simple_tag
def static_version(f):
    filename = static(f)
    filepath = settings.STATIC_ROOT + f
    return filename + '?v=' + str(os.stat(filepath).st_mtime)