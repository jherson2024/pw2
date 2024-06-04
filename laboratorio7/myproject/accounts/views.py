from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        email=request.POST["email"]
        if password1==password2:
         if User.objects.filter(username=username).exist():
            messages.info(request,"Username taken")
         elif User.objects.filter(email=email).exist():
            messages.info(request,"email taken")
         else:
           user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
           user.save();
           messages.info(request,"user created")
           return redirect("/")
        else: 
           messages.info(request,"password not matchine..")
    else:
        messages.info(request,request,"register.html")