from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def success(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, "success.html", context)

# def login(request):
#     if request.method == "POST":

#         errors = User.objects.validator(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#             return redirect('/')

#         user = User.objects.get(email=request.POST['email'])
#         if bcrypt.checkpw(password.encode(),user.password.encode()):
#             print("User Password Matches")
#             request.session["id"]=user.id
#             # request.session["first_name"]=user.first_name
#             return redirect("/wall")
#         else:
#             errors['username'] = "Username is incorrect"

#     if(len(errors)):
#         for tag, error in errors.items():
#             messages.error(request, error, extra_tags=tag)
#         return redirect('home')
#     else:
#         return redirect ('success', id=user.id)

def login(request):
    if request.method == "POST":

        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")

        user = User.objects.get(email=request.POST['loginEmail'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("User Password Matches")
            request.session["id"]=user.id
            request.session["first_name"]=user.first_name
            return redirect("/thewall/wall")
        else:
            print("User Password Match Fails")
            return redirect("/")

def register(request):
    errors = User.objects.validator(request.POST)
    
    if(len(errors)):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('home')
    else:
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        userName = request.POST.get('username')
        email = request.POST.get('email')
        hashed_password = bcrypt.hashpw(request.POST.get('password').encode(),bcrypt.gensalt()).decode()
        birthDate = request.POST.get('birthdate')
        User.objects.create(first_name=firstName, last_name=lastName, email=email, username=userName, password=hashed_password, birthdate=birthDate)
        user = User.objects.last()
        return redirect ('success', id=user.id)

def users(request):
    context = {
        'user_list': User.objects.all()
    }
    return render(request, "users.html", context)

def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')
