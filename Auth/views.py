from django.shortcuts import render, redirect
from django.contrib import messages  # Import the messages framework
from django.contrib.auth.models import User
from .forms import SignupForm
from .models import UserProfile

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
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html')