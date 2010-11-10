"""Edit tags file"""
from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.tag(name="edit_link")
def do_edit_link(parser, token):
    """Compilation function for edit_link tag"""
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, obj = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, \
        "%r tag requires a single argument" % \
        token.contents.split()[0]
    return FormatEditLinkNode(obj)


class FormatEditLinkNode(template.Node):
    """Format class for edit_link tag node"""
    def __init__(self, object_to_be_formatted):
        self.object_to_be_formatted = template.Variable(object_to_be_formatted)

    def render(self, context):
        try:
            obj = self.object_to_be_formatted.resolve(context)
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                  obj._meta.module_name),  args=[obj.id])
            return u'<a href="%s">Edit %s</a>' % (url,  obj.__unicode__())
        except template.VariableDoesNotExist:
            return ''
