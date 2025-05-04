import csv
from django.core.management.base import BaseCommand
from dashboard.models import Computer

class Command(BaseCommand):
    help = 'Import computers from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='/Users/medamineamma/Desktop/cmdb_ci_computer.csv')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Computer.objects.create(
                    name=row['Name'],
                    manufacturer=row['Manufacturer'] if row['Manufacturer'] != 'NULL' else None,
                    operating_system=row['Operating System'],
                    assigned_to=row['Assigned to'] if row['Assigned to'] != 'NULL' else None,
                    mac_address=row['MAC Address'] if row['MAC Address'] != 'NULL' else None,
                    model_id=row['Model ID'] if row['Model ID'] != 'NULL' else None,
                    serial_number=row['Serial number'] if row['Serial number'] != 'NULL' else None,
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully imported computers from {csv_file}'))