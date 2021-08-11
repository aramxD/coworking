import csv
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse 

# Librerias para agregar usuarios
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# Create your views here.


# signup users
def signupuser(request):

    context= {
    'form': UserCreationForm(),
    }


    if request.method == 'GET':
        return render(request, 'signupuser.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registro')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form': UserCreationForm() ,'error': 'User has been taken'})
        else:
            return render(request, 'signupuser.html', {'form': UserCreationForm() ,'error': 'Password did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect ('registro')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html',  {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form': AuthenticationForm() , 'error': 'User or password did not match'})
        else:
            login(request, user)
            return redirect('registro')


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


def listado_registro(request):
    listado = Registro.objects.all()
    context = {
        'listado': listado,
        
        }
    return render (request, 'listado.html', context)


def listado_export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Apeido', 'Email', 'Telefono', 'Entrada'])

    for registro in Registro.objects.all().values_list('nombre', 'apeido', 'email', 'telefono', 'fecha'):
        writer.writerow(registro)

    response['Content-Disposition'] = 'attachment; filename="registro.csv"'
    return response