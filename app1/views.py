from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import football

def registration(request):
    if request.method == 'POST':
        print(request.POST)
        ucl = football()
        ucl.club = request.POST.get('club')
        ucl.manager = request.POST.get('manager')
        ucl.stadium = request.POST.get('stadium')
        ucl.trophies = request.POST.get('trophies')
        ucl.country = request.POST.get('country')
        ucl.save()
        return redirect('/')
    return render(request,'registration.html')

def fetchall(request):
    fetch = football.objects.all()
    return render(request,'delete.html',{'fetch':fetch})

def delete(request,id):
    print(id)
    delete = football.objects.get(id=id)
    delete.delete()
    return redirect('/')

def update(request,id):
    print(id)
    update = football.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        update.club = request.POST.get('club')
        update.manager = request.POST.get('manager')
        update.stadium = request.POST.get('stadium')
        update.trophies = request.POST.get('trophies')
        update.country = request.POST.get('country')
        update.save()
        return redirect('/')
    return render(request,'update.html',{'update':update})

