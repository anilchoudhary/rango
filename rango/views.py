from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context_dict = {'bold_message': "This is so awsome to work with."}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': "Anil Choudhary"}
    return render(request, 'rango/about.html', context=context_dict)
