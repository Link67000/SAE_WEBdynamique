from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import EtudiantForm
from . import models
from .models import Etudiant, Absence

def ajout_Etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        return render(request, "Etudiant/ajout.html", {"form": form})
    else:
        form = EtudiantForm()  
        return render(request, "Etudiant/ajout.html", {"form": form})
    
def traitement(request):
    Etudiant_form = EtudiantForm(request.POST , request.FILES)
    if Etudiant_form.is_valid():
        Etudiant = Etudiant_form.save()
        return HttpResponseRedirect("/ABS/Etudiant/")
    else:
        return render(request, "Etudiant/ajout.html", {"form": Etudiant_form})

def index(request):
    liste = (models.Etudiant.objects.all())
    return render(request, "Etudiant/index.html", {"liste" : liste})

def affiche(request, id):
    etudiant = Etudiant.objects.get(pk=id)
    liste_absence = models.Absence.objects.filter(etudiant=etudiant)
    return render(request,"Etudiant/affiche.html", {"Etudiant" : etudiant, "liste_absence":liste_absence})


def update(request,id):
    Etudiant = models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(Etudiant.dico())
    return render(request, "Etudiant/ajout.html", {"form": form, "id": id})


def updatetraitement(request, id):
    etudiant = get_object_or_404(Etudiant, pk=id)
    
    if request.method == "POST":
        form = EtudiantForm(request.POST, request.FILES, instance=etudiant)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ABS/Etudiant/") 
        else:
            return render(request, "Etudiant/update.html", {"form": form, "id": id})
    else:
        form = EtudiantForm(instance=etudiant)
        return render(request, "Etudiant/update.html", {"form": form, "id": id})
    
def delete(request, id):
    Etudiant = models.Etudiant.objects.get(pk=id)
    Etudiant.delete()
    return HttpResponseRedirect("/ABS/Etudiant/")


#pdf 

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_pdf_view(request, id):
    etudiant= models.Etudiant.objects.get(pk=id)
    template_path = 'index/pdf.html'
    liste_absence = models.Absence.objects.filter(etudiant=etudiant)
    context = {'Etudiant': etudiant , "liste_absence":liste_absence}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if doawnload
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response