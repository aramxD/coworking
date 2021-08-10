from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
# Create your views here.


def registro(request):
    nuevo_registro = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                registro = form.save(commit=False)
                registro.save()
                
                
                return render (request, 'index.html', {'form':nuevo_registro})
            except ValueError:
                return render (request, 'index.html', {'form':nuevo_registro})
            
            
        else:
            pass

    else:
        context={
            'form':nuevo_registro
            }
    return render (request, 'index.html', context)