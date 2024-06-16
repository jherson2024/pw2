from django.shortcuts import render

# Create your views here.
def myHomeView(request,*args,**kwargs):
    myContext={
        "myText":"Esto es sobre nosotros",
        "myNumber":123,
        "myList":[33,44,55],
    }
    return render(request,"home.html",myContext)