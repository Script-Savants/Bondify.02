from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created  for ' + username)
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'front_v1/vikinger-dark/register.html', {'form': form})




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('success')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'front_v1/vikinger-dark/login.html')

    context = {}
    return render(request, 'front_v1/vikinger-dark/login.html', context)

@login_required(login_url='login')
def success(request):
    return render(request, 'success.html')


def logoutUser(request):
    logout(request)
    return redirect('login')



