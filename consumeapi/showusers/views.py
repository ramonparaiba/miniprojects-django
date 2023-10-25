from django.shortcuts import render
from django.http import HttpResponse
import requests

def show_users(request):
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    users = r.json()
    context = {
        'users' : users
    }
    return render(request, 'index.html', context)