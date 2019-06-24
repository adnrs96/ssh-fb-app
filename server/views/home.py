from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def handle_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')
