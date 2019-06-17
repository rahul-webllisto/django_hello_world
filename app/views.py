from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Language

def hello_world(request):
    return HttpResponse("HELLO WORLD!!!")

def languages(request):
    languages = Language.objects.all()
    return render(request, 'language.html', {'languages': languages})
