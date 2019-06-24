from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def render_real_home(request: HttpRequest) -> HttpResponse:
    ctx = {
        "name": request.user.full_name,
        "image_url": request.user.profile_picture.url
    }
    return render(request, 'home.html', ctx)
    return HttpResponse('Yeah you are logged in!')

def handle_home(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    return render_real_home(request)
