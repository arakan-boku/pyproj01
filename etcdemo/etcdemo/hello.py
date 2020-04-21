from django.template.context_processors import csrf
from django.shortcuts import render
from . import helloforms as forms
import os


def hello(request):
    if request.method == 'POST':
        c = {
            'name': request.POST["name"]
        }
    else:
        f = forms.HelloForm(label_suffix='：')
        c = {
            'form': f,
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__))),
        }
    c.update(csrf(request))
    return render(request, 'hello.html', c)
