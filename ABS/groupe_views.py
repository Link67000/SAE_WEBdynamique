from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import GroupeForm
from . import models , cours_views
from .models import Groupe





def ajout_Groupe(request):
    if request.method == "POST":
        form = GroupeForm(request.POST)
        return render(request, "Groupe/ajout.html", {"form": form})
    else:
        form = GroupeForm()  
        return render(request, "Groupe/ajout.html", {"form": form})
    

def traitement(request):
    Groupe_form = GroupeForm(request.POST)
    if Groupe_form.is_valid():
        Groupe = Groupe_form.save()
        return HttpResponseRedirect("/ABS/Groupe/")
    else:
        return render(request, "Groupe/ajout.html", {"form": Groupe_form})

def index(request):
    liste = (models.Groupe.objects.all())
    return render(request, "Groupe/index.html", {"liste" : liste})

def affiche(request, id):
    groupe = Groupe.objects.get(pk=id)
    liste_cours = models.Cours.objects.filter(groupe=groupe)
    liste = (models.Groupe.objects.all())
    return render(request,"Groupe/affiche.html", {"Groupe" : groupe, "liste_cours":liste_cours, "liste":liste})

def update(request,id):
    Groupe = models.Groupe.objects.get(pk=id)
    form = GroupeForm(Groupe.dico())
    return render(request, "Groupe/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    form = GroupeForm(request.POST)
    if form.is_valid():
        Groupe = form.save(commit=False)
        Groupe.id = id
        Groupe.save()
        return HttpResponseRedirect(f"/ABS/afficheGroupe/{Groupe.id}") 
    else:
        return render(request, "Groupe/update.html", {"form": form, "id": id})
    
def delete(request, id):
    Groupe = models.Groupe.objects.get(pk=id)
    Groupe.delete()
    return HttpResponseRedirect("/ABS/Groupe/")
