from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):

    context = {
        'name': '大聪明'
    }

    return render(request, 'book02/index.html', context)

