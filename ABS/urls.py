from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import absence_views, cours_views, enseignant_views, etudiant_views, groupe_views,views

urlpatterns = [


    path('', views.index),
    
    path('depotcsv/', absence_views.upload_csv),
    path('csv/', absence_views.export_absences_csv),
    path('ajoutAbsence/', absence_views.ajout_Absence),
    path('ajoutAbsence/<int:id>/', absence_views.ajout_Absence),
    path('traitementAbsence/<int:id>/', absence_views.traitement),
    path("Absence/", absence_views.index),
    path('afficheAbsence/<int:id>/', absence_views.affiche),
    path('updateAbsence/<int:id>/', absence_views.update),
    path('updatetraitementAbsence/<int:id>/', absence_views.updatetraitement),
    path('deleteAbsence/<int:id>/', absence_views.delete),
    path('deleteAbsence/<int:id>/', absence_views.delete),
    path('afficheEtudiant/<int:id>/pdf', etudiant_views.render_pdf_view),
    
    path('ajoutCours/', cours_views.ajout_Cours),
    path('traitementCours/', cours_views.traitement),
    path("Cours/", cours_views.index),
    path('afficheCours/<int:id>/', cours_views.affiche),
    path('updateCours/<int:id>/', cours_views.update),
    path('updatetraitementCours/<int:id>/', cours_views.updatetraitement),
    path('deleteCours/<int:id>/', cours_views.delete),
    
    path('ajoutEnseignant/', enseignant_views.ajout_Enseignant),
    path('traitementEnseignant/', enseignant_views.traitement),
    path("Enseignant/", enseignant_views.index),
    path('afficheEnseignant/<int:id>/', enseignant_views.affiche),
    path('updateEnseignant/<int:id>/', enseignant_views.update),
    path('updatetraitementEnseignant/<int:id>/', enseignant_views.updatetraitement),
    path('deleteEnseignant/<int:id>/', enseignant_views.delete),
    
    path('ajoutEtudiant/', etudiant_views.ajout_Etudiant),
    path('traitementEtudiant/', etudiant_views.traitement),
    path("Etudiant/", etudiant_views.index),
    path('afficheEtudiant/<int:id>/', etudiant_views.affiche),
    path('updateEtudiant/<int:id>/', etudiant_views.update),
    path('updatetraitementEtudiant/<int:id>/', etudiant_views.updatetraitement),
    path('deleteEtudiant/<int:id>/', etudiant_views.delete),
    
    path('ajoutGroupe/', groupe_views.ajout_Groupe),
    path('traitementGroupe/', groupe_views.traitement),
    path("Groupe/", groupe_views.index),
    path('afficheGroupe/<int:id>/', groupe_views.affiche),
    path('updateGroupe/<int:id>/', groupe_views.update),
    path('updatetraitementGroupe/<int:id>/', groupe_views.updatetraitement),
    path('deleteGroupe/<int:id>/', groupe_views.delete),

    path('afficheCours/<int:cours_id>/absence/form/<int:etudiant_id>/', absence_views.prefill_absence_form, name='prefill_absence_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
