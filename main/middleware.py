"""File where middleware defenitions are situated"""
from main.models import Request


class RequestHook:
    """Hooks each request"""
    def process_request(self, request):
        """Put each request to db"""
        Request.objects.create(request=request)
        return
