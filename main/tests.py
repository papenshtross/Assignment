"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from main.models import Profile, Request
from django_webtest import WebTest


class MainTest(WebTest):
    """Main unit tests class"""
    fixtures = ['initial_data.yaml']
    profile_pk = 1

    def test_index(self):
        """Test case for index page"""
        response = self.client.get('')

        # Check that the response is 200 OK
        self.failUnlessEqual(response.status_code, 200)
        # Check that index.html template is using
        self.assertTemplateUsed(response, 'index.html', msg_prefix='')
        # Assign profile objects from test db and acquired from response
        profile = Profile.objects.get(pk=self.profile_pk)
        response_profile = response.context['profile']
        # Check that response contains first_name filed value
        self.assertContains(response, profile.first_name,
                            count=1, msg_prefix='')
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
        self.client.get('')
        self.assertTrue(Request.objects.all().count() > 0)

    def test_django_template_processor(self):
        """Test case for django settings context template processor"""
        response = self.client.get('')
        context_settings = response.context['settings']
        self.assertIsNotNone(context_settings)

    def test_edit_profile(self):
        """Test case for edit profile"""
        response = self.app.get('/profile_edit/' +
                                str(self.profile_pk) + '/',
                                extra_environ=dict(REMOTE_USER='root'))
        response_form = response.context['form']
        self.assertIsNotNone(response_form)

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
