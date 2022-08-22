from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginView(request):
    context = {}
    if request.POST: 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            #return redirect('/main')
        else:
            context['auth'] = False
    return render(request, 'login.html', context)

def signupView(request):
    return render(request, 'signup.html', {})

@login_required(login_url='/login/')
def mainView(request):
    return render(request, 'main.html', {})