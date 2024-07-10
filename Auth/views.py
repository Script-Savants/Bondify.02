from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messages framework
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import UserProfile
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            UserProfile.objects.create(
                user=user,
                gender=request.POST['gender'],
                age=request.POST['age'],
                location=request.POST['location']
            )

            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Redirect to the home page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')