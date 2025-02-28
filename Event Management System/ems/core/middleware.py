from django.shortcuts import redirect
from django.conf import settings
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URLs to exclude from authentication
        excluded_urls = [settings.LOGIN_URL, '/accounts/signup/', '/accounts/logout/']

        # Get the current URL
        current_url = resolve(request.path_info).url_name

        if request.path not in excluded_urls and not request.user.is_authenticated:
            # Redirect to the login page if not authenticated
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
