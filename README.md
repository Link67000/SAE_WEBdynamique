# Gestion des Absences


  # Ce repository contient :
  - Le code complet du site 
  - un dossier contenant les fichiers de configurition d'apache2
  - un dossier contenant les schémas relationel de la base de donnée
  - un fichier avec les commandes/script pour creer la base de données sur MySql 


## Introduction
Ce projet a pour objectif de fournir une interface de gestion des absences pour un département universitaire. Les gestionnaires pourront saisir et valider les absences des étudiants pour différents cours, ainsi qu'ajouter des justifications pour ces absences. Le projet inclut un CRUD pour gérer les groupes d'étudiants, les étudiants, les enseignants, les cours et les absences.

## Schéma de Données

### Groupes d'Étudiants
- `id` (int) : Identifiant unique du groupe
- `nom` (string) : Nom du groupe

### Étudiants
- `id` (int) : Identifiant unique de l'étudiant
- `nom` (string) : Nom de famille de l'étudiant
- `prénom` (string) : Prénom de l'étudiant
- `email` (string) : Email de l'étudiant
- `groupe` (int) : Identifiant du groupe auquel l'étudiant appartient
- `photo` (string) : Lien vers la photo de l'étudiant

### Enseignants
- `id` (int) : Identifiant unique de l'enseignant
- `nom` (string) : Nom de famille de l'enseignant
- `prénom` (string) : Prénom de l'enseignant
- `email` (string) : Email de l'enseignant

### Cours
- `id` (int) : Identifiant unique du cours
- `titre` (string) : Titre du cours
- `date` (date) : Date du cours
- `enseignant` (int) : Identifiant de l'enseignant responsable du cours
- `durée` (int) : Durée du cours en minutes
- `groupe` (int) : Identifiant du groupe d'étudiants participant au cours

### Absences
- `étudiant` (int) : Identifiant de l'étudiant
- `cours` (int) : Identifiant du cours
- `justifié` (boolean) : Indique si l'absence est justifiée
- `justification` (string) : Justification de l'absence

## Fonctionnalités

### Gestion des Groupes
- Créer, lire, mettre à jour et supprimer des groupes d'étudiants.

### Gestion des Étudiants
- Créer, lire, mettre à jour et supprimer des étudiants.
- Lister les étudiants par groupe.

### Gestion des Enseignants
- Créer, lire, mettre à jour et supprimer des enseignants.

### Gestion des Cours
- Créer, lire, mettre à jour et supprimer des cours.
- Assigner des cours à des groupes d'étudiants.
- Associer un enseignant à un cours.

### Gestion des Absences
- Saisir des absences pour les étudiants inscrits à un cours.
- Valider les absences et ajouter des justifications.
- Importer les absences d'un cours via un fichier.
- Générer une fiche de liste des absences pour un cours spécifique.
- Générer une fiche des absences pour un étudiant, incluant le total des absences justifiées et non justifiées.


