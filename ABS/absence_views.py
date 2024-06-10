from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages
from .forms import AbsenceForm, UploadCSVForm
from . import models
from .models import Absence, Etudiant, Cours
import csv

def ajout_Absence(request):
    if request.method == "POST":
        form = AbsenceForm(request.POST)
        return render(request, "Absence/ajout.html", {"form": form})
    else:
        form = AbsenceForm()  
        return render(request, "Absence/ajout.html", {"form": form})
    
def prefill_absence_form(request, etudiant_id, cours_id):
    etudiant = models.Etudiant.objects.get(pk=etudiant_id)
    cours = models.Cours.objects.get(pk=cours_id)
    initial_data = {
        'etudiant': etudiant,
        'cours': cours,
        'justifie': 'NON',
        'justification': 'Aucune'
    }
    form = AbsenceForm(initial=initial_data)
    return render(request, 'Absence/ajout.html', {'form': form, 'etudiant': etudiant, "cours_id": cours_id})

def traitement(request, id):
    Absence_form = AbsenceForm(request.POST)
    if Absence_form.is_valid():
        Absence = Absence_form.save()
        return HttpResponseRedirect(f"/ABS/afficheCours/{id}/")
    else:
        return render(request, "Absence/ajout.html", {"form": Absence_form})

def index(request):
    liste = models.Absence.objects.all()
    return render(request, "Absence/index.html", {"liste" : liste})

def affiche(request, id):
    absence = Absence.objects.get(pk=id)
    liste = (models.Absence.objects.all())
    return render(request,"Absence/affiche.html", {"Absence" : absence, "liste":liste})

def update(request,id):
    Absence = models.Absence.objects.get(pk=id)
    form = AbsenceForm(Absence.dico())
    return render(request, "Absence/update.html", {"form": form, "id": id})



def updatetraitement(request, id):
    absence = models.Absence.objects.get(pk=id)
    form = AbsenceForm(request.POST,instance=absence)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f"/ABS/afficheEtudiant/{absence.etudiant.id}/") 
    else:
        return render(request, "Absence/update.html", {"form": form, "id": id})
    
def delete(request, id):
    Absence = models.Absence.objects.get(pk=id)
    Absence.delete()
    return HttpResponseRedirect(f"/ABS/afficheEtudiant/{Absence.etudiant.id}/")


def export_absences_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="absences.csv"'

    writer = csv.writer(response)
    writer.writerow(['etudiant', 'cours', 'justifie', 'justification'])

    absences = Absence.objects.all()
    for absence in absences:
        writer.writerow([absence.etudiant.id, absence.cours.id, absence.justifie, absence.justification])

    return response

def upload_csv(request):
    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                try:
                    etudiant = Etudiant.objects.get(pk=row['etudiant'])
                    cours = Cours.objects.get(pk=row['cours'])
                    justifie = row['justifie']
                    justification = row['justification'] if row['justification'] else None

                    absence, created = Absence.objects.get_or_create(
                        etudiant=etudiant,
                        cours=cours,
                        justifie=justifie,
                        justification=justification
                    )
                    if created:
                        messages.success(request, f"Absence for {etudiant} in {cours} created successfully.")
                    else:
                        messages.warning(request, f"Absence for {etudiant} in {cours} already exists.")
                except Etudiant.DoesNotExist:
                    messages.error(request, f"Etudiant with id {row['etudiant']} does not exist.")
                except Cours.DoesNotExist:
                    messages.error(request, f"Cours with id {row['cours']} does not exist.")
            
            return redirect('/ABS/')
    else:
        form = UploadCSVForm()
    return render(request, 'Absence/upload_csv.html', {'form': form})