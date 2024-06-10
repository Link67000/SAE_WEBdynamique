from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import EnseignantForm
from . import models
from .models import Enseignant

def ajout_Enseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        return render(request, "Enseignant/ajout.html", {"form": form})
    else:
        form = EnseignantForm()  
        return render(request, "Enseignant/ajout.html", {"form": form})
    
def traitement(request):
    Enseignant_form = EnseignantForm(request.POST)
    if Enseignant_form.is_valid():
        Enseignant = Enseignant_form.save()
        return HttpResponseRedirect("/ABS/Enseignant/")
    else:
        return render(request, "Enseignant/ajout.html", {"form": Enseignant_form})

def index(request):
    liste = (models.Enseignant.objects.all())
    return render(request, "Enseignant/index.html", {"liste" : liste})

def affiche(request, id):
    enseignant = Enseignant.objects.get(pk=id)
    return render(request,"Enseignant/affiche.html", {"Enseignant" : enseignant})

def update(request,id):
    Enseignant = models.Enseignant.objects.get(pk=id)
    form = EnseignantForm(Enseignant.dico())
    return render(request, "Enseignant/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    form = EnseignantForm(request.POST)
    if form.is_valid():
        Enseignant = form.save(commit=False)
        Enseignant.id = id
        Enseignant.save()
        return HttpResponseRedirect("/ABS/Enseignant/") 
    else:
        return render(request, "Enseignant/ajout.html", {"form": form, "id": id})
    
def delete(request, id):
    Enseignant = models.Enseignant.objects.get(pk=id)
    Enseignant.delete()
    return HttpResponseRedirect("/ABS/Enseignant/")