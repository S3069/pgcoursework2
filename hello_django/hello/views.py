# from django.shortcuts import render

# Create your views here.

# Original test script when first forming page. Prints "Hello, Django!" when
#   page at http://127.0.0.1:8000/ is opened

import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

#LogMessage Imports
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage

# Home Page
from django.views.generic import ListView

'''
# Home 1
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
# Home 2
'''
def home(request):
    return render(request, "hello/home.html")
'''

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

# LogMessage
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
    

#Home 3
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context