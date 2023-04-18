from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.templatetags.static import static


def css(request):
    css_url = static('index-b2f606c3.css')
    with open(css_url, 'r') as f:
        css = f.read()
    response = HttpResponse(css, content_type='text/css')
    return response
