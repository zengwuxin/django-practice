from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index (request):
    return HttpResponse ("Hello, you're at the Poll Index")

def suggestions(request):
    return render(request, 'polls/suggestions.html' ,{})