from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpRequest, HttpResponse

def handle_login(request: HttpRequest) -> HttpResponse:
    fb_oauth_uri = 'https://www.facebook.com/v3.3/dialog/oauth?client_id=%s&redirect_uri=%s'
    return redirect(fb_oauth_uri % (settings.FACEBOOK_APP_ID, settings.ROOT_DOMAIN_URI + '/postlogin'))

def handle_post_login(request: HttpRequest) -> HttpResponse:
    error = request.GET.get('error')
    if error is not None:
        return render(request, "login_error.html")
    return HttpResponse('We will login you shortly!')
