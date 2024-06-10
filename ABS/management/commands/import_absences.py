import csv
import os
import django
from django.core.management.base import BaseCommand
from models import Absence, Etudiant, Cours

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "votre_projet.settings")
django.setup()

class Command(BaseCommand):
    help = 'Import absences from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
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
                        self.stdout.write(self.style.SUCCESS(f"Absence for {etudiant} in {cours} created successfully."))
                    else:
                        self.stdout.write(self.style.WARNING(f"Absence for {etudiant} in {cours} already exists."))
                except Etudiant.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Etudiant with id {row['etudiant']} does not exist."))
                except Cours.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Cours with id {row['cours']} does not exist."))