from django.shortcuts import render
from django.http import HttpResponse

def NewAccount(request):
    return render(request, 'NewAccount.html')
