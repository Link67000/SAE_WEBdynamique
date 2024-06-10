
from django.http import HttpResponseRedirect
from .forms import CoursForm, AbsenceForm
from . import models
from .models import Cours, Groupe, Etudiant, Absence
from django.shortcuts import render, get_object_or_404, redirect


def ajout_Cours(request):
        form = CoursForm()
        return render(request, "Cours/ajout.html", {"form": form} )


    

def traitement(request):
    Cours_form = CoursForm(request.POST)
    if Cours_form.is_valid():
        Cours = Cours_form.save()
        return HttpResponseRedirect("/ABS/Groupe/")
    else:
        return render(request, "Cours/ajout.html", {"form": Cours_form})




def index(request):
    liste = (models.Cours.objects.all())
    return render(request, "Cours/index.html", {"liste" : liste})

def affiche(request, id):
    groupe = Cours.objects.get(pk=id).groupe
    cours = Cours.objects.get(pk=id)
    liste_etudiant = models.Etudiant.objects.filter(groupe=groupe)
    return render(request,"Cours/affiche.html", {"Cours" : cours,"liste_etudiant":liste_etudiant})


def update(request,id):
    Cours = models.Cours.objects.get(pk=id)
    form = CoursForm(Cours.dico())
    return render(request, "Cours/update.html", {"form": form, "id": id})



def updatetraitement(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(request.POST,instance=cours)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ABS/Groupe/") 
    else:
        return render(request, "Cours/update.html", {"form": form, "id": id})
    

    
def delete(request, id):
    Cours = models.Cours.objects.get(pk=id)
    Cours.delete()
    return HttpResponseRedirect(f"/ABS/afficheGroupe/{Cours.groupe.id}")





