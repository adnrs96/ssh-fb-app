from django.shortcuts import redirect, render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
import requests

def handle_login(request: HttpRequest) -> HttpResponse:
    fb_oauth_uri = 'https://www.facebook.com/v3.3/dialog/oauth?client_id=%s&redirect_uri=%s'
    return redirect(fb_oauth_uri % (settings.FACEBOOK_APP_ID, settings.ROOT_DOMAIN_URI + '/postlogin'))

def handle_post_login(request: HttpRequest) -> HttpResponse:
    error = request.GET.get('error')
    code = request.GET.get('code')
    if error is not None or code is None:
        return render(request, "login_error.html")

    # Exchange code for access_token.
    fb_oauth_access_token_uri = 'https://graph.facebook.com/v3.3/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s'
    res_to_access_token_req = requests.get(fb_oauth_access_token_uri % (
        settings.FACEBOOK_APP_ID,
        settings.ROOT_DOMAIN_URI + '/postlogin',
        settings.FACEBOOK_APP_SECRET,
        code
    ))
    data = res_to_access_token_req.json()
    access_token = data.get('access_token')
    if access_token is None:
        logging.error('Could not retrieve access_token. %s : %s' % (data.get('error'), data.get('error_description')))
        return render(request, "error.html")

    # Inspect access_token to grab a user_id
    fb_graph_debug_token = 'https://graph.facebook.com/debug_token?input_token=%s&access_token=%s|%s'
    res_token_inspect_req = requests.get(fb_graph_debug_token % (
        access_token, settings.FACEBOOK_APP_ID,
        settings.FACEBOOK_APP_SECRET
    ))
    user_data = res_token_inspect_req.json()
    if user_data.get('error') is not None:
        logging.error('Could not retrieve access_token. %s' % (user_data.get('error').get('message')))
        return render(request, "error.html")

    return HttpResponse('We will login you shortly!')
