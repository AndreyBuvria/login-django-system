from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def loginView(request):
    context = {}
    if request.POST: 
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            context['auth'] = False
    return render(request, 'login.html', context)

def signupView(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password-1']

        if password == password_check:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                
                return redirect('main')

    return render(request, 'signup.html', {})

@login_required(login_url='login')
def mainView(request):
    return render(request, 'main.html', {})