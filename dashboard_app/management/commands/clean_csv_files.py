from django.core.management.base import BaseCommand
from django.conf import settings
from dashboard_app.models import CSVData
import os
import shutil


class Command(BaseCommand):
    help = 'Clean all uploaded CSV files and database records'

    def add_arguments(self, parser):
        parser.add_argument(
            '--keep-sample',
            action='store_true',
            help='Keep sample_data.csv file',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Skip confirmation prompt',
        )

    def handle(self, *args, **options):
        # Clear database records
        csv_count = CSVData.objects.count()
        
        if csv_count == 0:
            self.stdout.write(
                self.style.WARNING('No CSV records found in database.')
            )
            return
        
        # Show what will be deleted
        self.stdout.write(f'Found {csv_count} CSV records in database:')
        for csv_data in CSVData.objects.all():
            self.stdout.write(f'  - {csv_data.name} (uploaded: {csv_data.uploaded_at})')
        
        # Confirmation prompt
        if not options['force']:
            confirm = input('\nAre you sure you want to delete all CSV files? (yes/no): ')
            if confirm.lower() not in ['yes', 'y']:
                self.stdout.write(self.style.WARNING('Operation cancelled.'))
                return
        
        # Clear database records
        CSVData.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f'Deleted {csv_count} CSV records from database')
        )
        
        # Clean CSV files directory
        csv_dir = os.path.join(settings.MEDIA_ROOT, 'csv_files')
        
        if os.path.exists(csv_dir):
            if options['keep_sample']:
                # Keep only sample_data.csv
                files_deleted = 0
                for filename in os.listdir(csv_dir):
                    if filename != 'sample_data.csv':
                        file_path = os.path.join(csv_dir, filename)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            files_deleted += 1
                            self.stdout.write(f'Deleted: {filename}')
                
                self.stdout.write(
                    self.style.SUCCESS(f'Cleaned {files_deleted} CSV files (kept sample_data.csv)')
                )
            else:
                # Remove all files
                files_before = os.listdir(csv_dir)
                shutil.rmtree(csv_dir)
                os.makedirs(csv_dir, exist_ok=True)
                self.stdout.write(
                    self.style.SUCCESS(f'Cleaned all {len(files_before)} CSV files')
                )
        else:
            os.makedirs(csv_dir, exist_ok=True)
            self.stdout.write('Created CSV directory')
        
        self.stdout.write(
            self.style.SUCCESS('CSV files cleanup completed successfully!')
        )
