"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from main.models import Profile, Request, TransactionSignal
from django_webtest import WebTest
from django.template import Template, TemplateSyntaxError
from django.core.management import call_command
import sys
from StringIO import StringIO
from django.template.context import Context
from django.test.client import Client


class MainTest(WebTest):
    """Main unit tests class"""
    fixtures = ['initial_data.yaml']
    profile_pk = 1

    def test_index(self):
        """Test case for index page"""
        response = self.app.get('', extra_environ=dict(REMOTE_USER='root'))

        # Check that the response is 200 OK
        self.failUnlessEqual(response.status_int, 200)
        # Assign profile objects from test db and acquired from response
        profile = Profile.objects.get(pk=self.profile_pk)
        response_profile = response.context['profile']
        # Check that response contains first_name filed value
        assert profile.first_name in response, response
        # Check profile fields values
        self.failUnlessEqual(profile.first_name, response_profile.first_name)
        self.failUnlessEqual(profile.last_name, response_profile.last_name)
        self.failUnlessEqual(profile.bio, response_profile.bio)
        self.failUnlessEqual(profile.cell, response_profile.cell)
        self.failUnlessEqual(profile.icq, response_profile.icq)
        self.failUnlessEqual(profile.email, response_profile.email)
        self.failUnlessEqual(profile.skype, response_profile.skype)

    def test_request_hook_middleware(self):
        """Test case for request hook middleware"""
        self.app.get('', extra_environ=dict(REMOTE_USER='root'))
        self.assertTrue(Request.objects.all().count() > 0)

    def test_django_template_processor(self):
        """Test case for django settings context template processor"""
        response = self.app.get('', extra_environ=dict(REMOTE_USER='root'))
        context_settings = response.context['settings']
        self.assertNotEqual(context_settings, None)

    def test_edit_profile(self):
        """Test case for edit profile"""
        response = self.app.get('/profile_edit/' +
                                str(self.profile_pk) + '/',
                                extra_environ=dict(REMOTE_USER='root'))
        response_form = response.context['form']
        self.assertNotEqual(response_form, None)

    def test_edit_profile_webtest(self):
        """Test edit profile functionality using django_webtest"""
        form = self.app.get('/profile_edit/' + str(self.profile_pk) + '/',
                            extra_environ=dict(REMOTE_USER='root')).form
        test_name = 'test_name'
        form['first_name'] = test_name
        #Submit form and get following response
        response = form.submit().follow()  # all form fields are submitted
        #Check that response contains changed name
        self.failUnlessEqual(test_name, response.context['profile'].first_name)
        #Check that DB is updated
        profile = Profile.objects.get(pk=self.profile_pk)
        self.failUnlessEqual(test_name, profile.first_name)

    def test_login(self):
        """Test login functionality"""
        response = self.app.get('/profile_edit/' + str(self.profile_pk) + '/')
        self.failUnlessEqual(response.status_int, 302)
        form = response.follow().form
        self.assertNotEqual(form, None)
        self.assertNotEqual(form['username'], None)
        self.assertNotEqual(form['password'], None)
        response = self.app.get('/profile_edit/' + str(self.profile_pk) + '/',
                                extra_environ=dict(REMOTE_USER='root'))
        self.failUnlessEqual(response.status_int, 200)

    def test_birth_date_widget(self):
        """Test to ensure that date widget is presented"""
        response = self.app.get('/profile_edit/' +
                                str(self.profile_pk) + '/',
                                extra_environ=dict(REMOTE_USER='root'))
        assert 'DateTimeShortcuts' in response, response

    def test_reverse_field_order(self):
        """Test edit profile form reverse field order"""
        response = self.app.get('/profile_edit/' +
                                str(self.profile_pk) + '/',
                                extra_environ=dict(REMOTE_USER='root'))
        profile_fields = Profile._meta.fields[:]
        profile_fields.reverse()
        form_fields = response.form.fields.keys()
        self.assertEquals(profile_fields[-2].get_attname(), form_fields[1])

    def test_edit_link_tag(self):
        """Test case for edit_link template tag"""
        profile = Profile.objects.get(pk=self.profile_pk)
        self.assertRaises(TemplateSyntaxError, Template,
                          '{% load edit_tags %}{% edit_link %}')
        template = Template('{% load edit_tags %}{% edit_link profile %}')
        context = Context({"profile": profile})
        rendered = template.render(context)
        self.assertEqual(rendered, '<a href="/admin/main/profile/' +
                                   str(self.profile_pk) + '/">Edit ' +
                                   str(profile) + '</a>')

    def test_print_models_command(self):
        """Test case for print_models command"""
        stdout = []
        #Replace sys.stdout with capture buffer
        stdout.append(sys.stdout)
        _buf = StringIO()
        sys.stdout = _buf
        call_command('print_models', 'main')
        #Captured stdout output.
        result = _buf.getvalue()
        assert Profile.__name__ + '\n' + 'Objects count: ' +\
               str(len(Profile.objects.all())) in  result, result
        #Restore stdout
        if stdout:
            sys.stdout = stdout.pop()

    def test_signal_processor(self):
        """Test case for signal processor"""
        Profile.objects.create(first_name='test_name',
                               last_name='test_last_name',
                               birth_date='1988-09-22')
        #Test create signal
        create_transactions = TransactionSignal.objects.filter(
                model=Profile.__name__, action='create')
        assert len(create_transactions) > 0
        #Test update signal
        profile = Profile.objects.get(first_name='test_name',
                                      last_name='test_last_name')
        profile.first_name = 'test'
        profile.save()
        update_transactions = TransactionSignal.objects.filter(
                model=Profile.__name__, action='update')
        assert len(update_transactions) > 0
        #Test delete signal
        profile.delete()
        delete_transactions = TransactionSignal.objects.filter(
                model=Profile.__name__, action='delete')
        assert len(delete_transactions) > 0

    def test_ajax_form(self):
        """Test case for ajax form view"""
        form = self.app.get('/contact/').form
        form['subject'] = "test_subject"
        form['text'] = "test_text"
        #Submit form and get following response
        response = form.submit()
        #Not ajax
        self.failUnlessEqual(response.status_int, 302)
        client = Client()
        #Form is valid
        response = client.post('/contact/', {'subject': 'test_subject',
                                             'text': 'test_text', },
                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        assert '"bad": "false"' in response.content, response.content
        #Form isn't valid
        response = client.post('/contact/', {'subject': '',
                                             'text': 'test_text', },
                               HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        assert '"bad": "true"' in response.content, response.content

    def test_request_list(self):
        """Test case for request list"""
        response = self.app.get('/request_list/')
        self.failUnlessEqual(response.status_int, 200)
        request_list = response.context['object_list']
        assert len(request_list) > 0 and len(request_list) <= 10

    def test_request_priority(self):
        """Unit test for request priority"""
        self.app.get('/request_list/')
        Request.objects.create(request='test_p_1', priority=1)
        Request.objects.create(request='test_p_2', priority=2)
        response = self.app.get('/request_list/')
        request_list = response.context['object_list']
        assert request_list[0].priority == 2, request_list[0].priority
