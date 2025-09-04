import pandas as pd
from django.core.management.base import BaseCommand
from programs.models import Program


class Command(BaseCommand):
    help = 'Import data from a public Google Sheet using pandas'

    def add_arguments(self, parser):
        parser.add_argument('sheet_url', type=str)

    def handle(self, *args, **options):
        # Convert Google Sheet URL to CSV export URL
        sheet_url = options['sheet_url']
        spreadsheet_id = sheet_url.split('/d/')[1].split('/')[0]
        csv_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=0"

        # Read the CSV data using pandas
        try:
            df = pd.read_csv(csv_url, header=0, skiprows=[0])
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error reading CSV: {e}"))
            return

        # Clear existing data (optional, remove if you want to append)
        Program.objects.all().delete()

        # Import data
        for index, row in df.iterrows():
            try:
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
                    link_for_detailed_info=row.get('Link for detailed info', ''),
                    data_source=row.get('Data Source', ''),
                    application_channel=row.get('Application Channel', ''),
                    added_by=row.get('Added by', '')
                )
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error importing row {row['SN']}: {e}"))
                continue

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(df)} programs'))
