import csv
from django.core.management.base import BaseCommand
from programs.models import Program

class Command(BaseCommand):
    help = 'Import data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Program.objects.create(
                    sn=int(row['SN']),
                    university_name=row['University Name'],
                    type_of_institution=row['Type of institution'],
                    location=row['Location'],
                    program_name=row['Program Name'],
                    degree=row['Degree'],
                    duration=row['Duration'],
                    instruction_language=row['Instruction Language'],
                    tuition_fee=row['Tuition Fee'],
                    semester_contribution=row['Semester contribution (Approx. per semester)'],
                    deadline=row['Deadline'],
                    beginning=row['Beginning'],
                    admission_restricted=row['Admission Restricted?'],
                    academic_requirements=row['Academic Requirements'],
                    ects=row['ECTS'],
                    grade_threshold=row['Grade Threshold'],
                    language_requirement=row['Language Requirement'],
                    link_for_detailed_info=row['Link for detailed info'],
                    data_source=row['Data Source'],
                    application_channel=row['Application Channel'],
                    added_by=row['Added by']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))