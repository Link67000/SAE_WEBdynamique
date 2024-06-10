from django.db import models

class Enseignant(models.Model):
    nom_Enseignant = models.CharField(max_length=15) 
    prenom_Enseignant = models.CharField(max_length=15) 
    email_Enseignant = models.CharField(max_length=25) 
    
    def __str__(self):
        return f"{self.nom_Enseignant} {self.prenom_Enseignant}"

    def dico(self):
        return {"nom_Enseignant":self.nom_Enseignant, "prenom_Enseignant":self.prenom_Enseignant, "email_Enseignant":self.email_Enseignant}
    

##############################    
cours_choice = {
    "FRANCAIS": "Français",
    "ALLEMAND": "Allemand",
    "ANGLAIS": "Anglais",
    "MATHEMATIQUES": "Mathématique",
    "PHYSIQUE CHIMIE": "Physique chimie",
}
duree_choice = {
    "1H30": "1H30",
    "3H": "3H",
}
class Cours(models.Model):
    titre_Cours = models.CharField(max_length=100, choices=cours_choice, default=None) 
    date_Cours = models.DateField(null=True, blank=True) 
    Enseignant = models.ForeignKey(Enseignant,db_column="Enseignant_id", on_delete=models.CASCADE, default=None) 
    durée_Cours = models.CharField(max_length=100, choices=duree_choice, default=None) 
    groupe = models.ForeignKey("Groupe",db_column="groupe_id", on_delete=models.CASCADE, default=None)  
    

    def __str__(self):
        return f"{self.titre_Cours} " 

    def dico(self):
        return {"titre_Cours":self.titre_Cours, "date_Cours":self.date_Cours, "Enseignant":self.Enseignant, "durée_Cours":self.durée_Cours, "groupe":self.groupe}
    
##############################   
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    groupe = models.ForeignKey("Groupe",db_column="groupe_id", on_delete=models.CASCADE, related_name='etudiants', default=None)
    photo = models.ImageField(null=True, blank=True, upload_to='photos/')

    def __str__(self):
        return f"{self.nom} {self.prenom} "
    
    
    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom, "email":self.email, "groupe":self.groupe, "photo":self.photo}
    
    
##############################   
class Absence(models.Model):
    etudiant = models.ForeignKey("Etudiant",db_column="etudiant_id", on_delete=models.CASCADE, related_name='absences') 
    cours = models.ForeignKey(Cours,db_column="cours_id", on_delete=models.CASCADE, related_name='absences', default=None)
    justifie = models.CharField(max_length=3, choices=[("OUI", "OUI"), ("NON", "NON")], default="NON")
    justification = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.justifie
    
    def dico(self):
        return {"etudiant":self.etudiant, "cours":self.cours, "justifie":self.justifie, "justification":self.justification}
    
##############################  
class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
    def dico(self):
        return {"nom":self.nom}