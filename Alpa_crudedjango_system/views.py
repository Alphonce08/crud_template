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

        query = People(name=name, email=email, idnum=idnum, age=age, gender=gender)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def index(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return redirect(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        idnum = request.POST.get('idnum')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit = People.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.idnum = idnum
        edit.age = age
        edit.gender = gender
        edit.save()
        return redirect("/")
    d = People.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
