# from django.shortcuts import render

# Create your views here.

# Original test script when first forming page. Prints "Hello, Django!" when
#   page at http://127.0.0.1:8000/ is opened

import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

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