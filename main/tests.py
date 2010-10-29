"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from main.models import Profile


class MainTest(TestCase):
    """Main unit tests class"""
    fixtures = ['initial_data.yaml']

    def test_index(self):
        """Test case for index page"""
        response = self.client.get('')

        # Check that the response is 200 OK
        self.failUnlessEqual(response.status_code, 200)
        # Check that index.html template is using
        self.assertTemplateUsed(response, 'index.html', msg_prefix='')
        # Assign profile objects from test db and acquired from response
        profile = Profile.objects.get(pk=1)
        response_profile = response.context['profile']
        # Check that response contains first_name filed value
        self.assertContains(response, profile.first_name, count=1,
                            status_code=200, msg_prefix='')
        # Check profile fields values
        self.failUnlessEqual(profile.first_name, response_profile.first_name)
        self.failUnlessEqual(profile.last_name, response_profile.last_name)
        self.failUnlessEqual(profile.bio, response_profile.bio)
        self.failUnlessEqual(profile.cell, response_profile.cell)
        self.failUnlessEqual(profile.icq, response_profile.icq)
        self.failUnlessEqual(profile.email, response_profile.email)
        self.failUnlessEqual(profile.skype, response_profile.skype)
