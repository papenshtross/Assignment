"""Contains widgets"""
from django.utils.encoding import force_unicode
from django.conf import settings
from django import forms
from django.utils.safestring import mark_safe
import datetime
import time

# DATETIMEWIDGET
import django


calbtn = u"""<img src="%s/site_media/jscalendar/img.gif"
alt="calendar" id="%s_btn" style="cursor: pointer; border:
1px solid #8888aa;" title="Select date and time"
            onmouseover="this.style.background='#444444';"
            onmouseout="this.style.background=''" />
<script type="text/javascript">
    Calendar.setup({
        inputField     :    "%s",
        ifFormat       :    "%s",
        button         :    "%s_btn",
        singleClick    :    true,
        showsTime      :    false
    });
</script>"""


class DateTimeWidget(forms.widgets.TextInput):
    """DateTime calendar widget"""
    dformat = '%Y-%m-%d'

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            try:
                final_attrs['value'] = \
                                   force_unicode(value.strftime(self.dformat))
            except:
                final_attrs['value'] = \
                                   force_unicode(value)
        if 'id' not in final_attrs:
            final_attrs['id'] = u'%s_id' % (name)
        id = final_attrs['id']
        #.replace('%', '%%')
        jsdformat = self.dformat
        cal = calbtn % (settings.MEDIA_URL, id, id, jsdformat, id)
        a = u'<input%s />%s' % (forms.util.flatatt(final_attrs), cal)
        return mark_safe(a)

    def value_from_datadict(self, data, files, name):
        dtf = django.utils.formats.get_format('DATETIME_INPUT_FORMATS')
        empty_values = forms.fields.EMPTY_VALUES

        value = data.get(name, None)
        if value in empty_values:
            return None
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            return datetime.datetime(value.year, value.month, value.day)
        for format in dtf:
            try:
                return datetime.datetime(*time.strptime(value, format)[:6])
            except ValueError:
                continue
        return None

    class Media:
        """Media files"""
        css = {
            'all': ('/site_media/jscalendar/calendar-win2k-cold-2.css', )
        }
        js = ('/site_media/jscalendar/calendar.js',
              '/site_media/jscalendar/lang/calendar-en.js',
              '/site_media/jscalendar/calendar-setup.js',
              )
