"""Contains widgets"""
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.utils import datetime_safe


DATE_FORMAT = '%m/%d/%y'


class DatePickerWidget(widgets.Widget):
    """DatePicker widget"""
    def render(self, name, value, attrs=None):
        """Widget render method"""
        if value is None:
            vstr = ''
        elif hasattr(value, 'strftime'):
            vstr = datetime_safe.new_datetime(value).strftime(DATE_FORMAT)
        else:
            vstr = value
        id = "id_%s" % name
        args = [
            "<input type=\"text\" value=\"%s\" name=\"%s\" id=\"%s\" />" % \
            (vstr, name, id),
            "<script type=\"text/javascript\">$(\"#%s\") \
            .datepicker({dateFormat:'mm/dd/y'});</script>" % id
            ]
        return mark_safe("\n".join(args))

    class Media:
        """Media files"""
        css = {
            'all': ('/site_media/css/jquery-ui-1.8.7.custom.css', )
        }
        js = ('/site_media/js/jquery-1.4.4.js',
              '/site_media/js/jquery-ui-1.8.7.custom.min.js', )
