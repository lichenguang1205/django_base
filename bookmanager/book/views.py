from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):

    context = {
        'name':'马上双11了，想要惊喜吗？'
    }
    # return HttpResponse("ok")
    return render(request, 'book/index.html', context)