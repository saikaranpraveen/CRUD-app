from django.shortcuts import render, redirect
from crud_app.forms import profileForm
from crud_app.models import profile
from django.views.decorators.csrf import csrf_protect

def pro(request):
    if request.method == "POST":
        form = profileForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect ("/show/")
            except:
                pass
    else:
        form = profileForm()
    return render(request, "index.html", {'form':form})  


def show(request):
    profiles = profile.objects.all()
    return render(request,"show.html",{'profiles':profiles})

def edit(request, id):
    profiles = profile.objects.get(id = id)
    return render(request,"edit.html", {'profiles':profiles})

def update(request, id):
    profiles = profile.objects.get(id = id)
    form = profileForm(request.POST, instance = profiles)
    if form.is_valid():
        form.save()
        return redirect('/show/')
    return render(request,"edit.html", {"profiles" : profiles})

def delete(request, id):
    profiles = profile.objects.get(id = id)
    profiles.delete()
    return redirect("/show")    