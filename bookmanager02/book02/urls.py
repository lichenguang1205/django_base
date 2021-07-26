from django.urls import path
from book02.views import index

urlpatterns = [
    path('index/', index)
]

