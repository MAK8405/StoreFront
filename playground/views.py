from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> response
# request handler
# action


def sayHello(request):
    # Pull data from db
    # Transform
    # Send email
    # return HttpResponse("Hello World")
    return render(request, "hello.html", {"name": "MAK8405"})
