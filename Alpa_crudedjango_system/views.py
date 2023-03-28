from django.shortcuts import render, redirect
from .models import People

def displayindex(request):
    return render(request, "index.html")

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnum = request.POST.get('idnum')
        age = request.POST.get('age')
        gender = request.POST.get('gender')


        query = People(name = name, email = email, age = age, gender = gender)
        query.save()
        return redirect("/")

    return render(request, "index.html")

def index(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)