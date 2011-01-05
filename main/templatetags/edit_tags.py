"""Edit tags file"""
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(obj):
    """Shortcut for edit_link tag"""
    url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
          obj._meta.module_name),  args=[obj.id])
    return u'<a href="%s">Edit %s</a>' % (url,  obj.__unicode__())
