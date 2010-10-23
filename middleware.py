from main.models import Request

__author__ = 'Romchig'

"""Middleware for http requests hooking"""
class RequestsHook:

    def process_request(self, request):
        """Put each request to db"""
        Request.objects.create(request=request)
        return