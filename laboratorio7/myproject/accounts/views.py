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
         if User.objects.filter(username=username).exists():
            messages.info(request,"Username taken")
            messages_list = list(messages.get_messages(request))
            return render(request, "register.html", {"messages": messages_list})
         elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")
            messages_list = list(messages.get_messages(request))
            return render(request, "register.html", {"messages": messages_list})
         else:
           user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
           user.save();
           messages.info(request,"user created")
           messages_list = list(messages.get_messages(request))
           return redirect("login", {"messages": messages_list})
        else: 
           messages.info(request,"password not matchine..")
           messages_list = list(messages.get_messages(request))
           return render(request, "register.html", {"messages": messages_list})
    else:
        return render(request,"register.html")
    
def login(request):
   if request.method=="POST":
      username=request.POST["username"]
      password=request.POST["password"]
      user=auth.authenticate(username=username,password=password)
      if user is not None:
         auth.login(request,user)
         messages.info(request,"user login")
         messages_list = list(messages.get_messages(request))
         return render(request,"login.html", {"messages": messages_list})
      else:
         messages.info(request,"invalid credentials")
         messages_list = list(messages.get_messages(request))
         return render(request, "login.html", {"messages": messages_list})
   else:
        return render(request,"login.html")
   
def login(request):
   auth.logout(request)
   return redirect("/")