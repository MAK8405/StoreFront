from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> response
# request handler
# action


def calculate():
    x = 1
    y = 2
    return x


def sayHello(request):
    # Pull data from db
    # Transform
    # Send email
    # return HttpResponse("Hello World")
    x = calculate()
    return render(request, "hello.html", {"name": "MAK8405"})
