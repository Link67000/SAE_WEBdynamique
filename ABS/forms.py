from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nom_Enseignant', 'prenom_Enseignant', 'email_Enseignant')
        labels = {
            'nom_Enseignant': _('Nom de l\'enseignant'),
            'prenom_Enseignant': _('Prénom de l\'enseignant'),
            'email_Enseignant': _('Email de l\'enseignant')
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre_Cours', 'date_Cours', 'Enseignant', 'durée_Cours', 'groupe')
        labels = {
            'titre_Cours': _('Titre du cours'),
            'date_Cours': _('Date du cours'),
            'Enseignant': _('Enseignant du cours'),
            'durée_Cours': _('Durée du cours'),
            'groupe': _('Groupes du cours'),
        }

class AbsenceForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = ('etudiant', 'cours', 'justifie', 'justification')
        labels = {
            'etudiant': _('Étudiant'),
            'cours': _('Cours'),
            'justifie': _('Justifié'),
            'justification': _('Justification'),
        }


class GroupeForm(ModelForm):
    class Meta:
        model = models.Groupe
        fields = ('nom',)
        labels = {
            'nom': _('Nom du groupe'),
        }

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom', 'prenom', 'email', 'groupe', 'photo')
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'email': _('Email'),
            'groupe': _('Groupe'),
            'photo': _('Photo'),
        }
        
class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()