# from django.shortcuts import render

# Create your views here.

# Original test script when first forming page. Prints "Hello, Django!" when
#   page at http://127.0.0.1:8000/ is opened

import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

'''
def home(request):
    return HttpResponse("Hello, Django!")
'''

'''
# Old hello_there function to display plain text webpage
def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %Y at %X")         # (Capitalise a, b, or y to output full date, month, year format) 

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)
'''

# New hello_there function to render page with a template
def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Replaced the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")