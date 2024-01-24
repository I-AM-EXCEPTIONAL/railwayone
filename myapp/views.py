from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("This is my app")

def About(request):
    return render(request, "About.html")
    #return HttpResponse("This is about page")

def Contact(request):
    return render(request, "Contact.html")
    #return HttpResponse("This is Contact page")

def Services(request):
    return render(request,"Services.html")
    #return HttpResponse("This is Services page")