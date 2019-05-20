from .models import User
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def connect(request):
    return render(request, 'login/connect.html', {})

def create(request):
    return render(request, 'login/create.html', {})

def connexion(request):
    username = request.GET['name']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
    # A backend authenticated the credentials
        login(request, user)
        return render(request, 'login/account.html', {
            'user':user,
        })
    else:
    # No backend authenticated the credentials
        return render(request, 'login/connect.html', {
            'error_message': "Nom d'utilisateur ou Mot de Passe incorrect",
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:connect'))

def creation(request):
    use = request.POST['name']
    try:
        man = User.objects.get(username=use)
    except:
        first = request.POST['first']
        last = request.POST['last']
        mail = request.POST['mail']
        passw = request.POST['password']
        user = User.objects.create_user(username=use,password=passw,email=mail, first_name = first, last_name= last)
        login(request, user)
        return render(request, 'login/account.html', {
            'user':user,
        })
    return render(request, 'login/create.html', {
        'error_message':"Nom d'utilisateur déjà utilisé !"
    })

from django.contrib.auth.decorators import login_required

#@login_required
def modif(request, user):
    utilisateur=request.user
    return render(request, 'login/modif.html', {user:utilisateur})

#@login_required
def enreg(request, user):
    utilisateur = request.user
    mail = request.POST['mail']
    utilisateur.email = mail
    utilisateur.save()
    return render(request, 'login/account.html', {user:utilisateur})