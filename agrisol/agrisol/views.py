from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User


def home(request):
    return render(request,"home.html")

def farmer(request):
    return render(request,"farmer.html")
