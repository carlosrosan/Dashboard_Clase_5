#!/usr/bin/env python
"""
Script to clean CSV files from memory and database
Run with: python clean_data.py
"""

import os
import sys
import django
import shutil

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_project.settings')
django.setup()

from django.conf import settings
from dashboard_app.models import CSVData

def clean_csv_data():
    """Clean all CSV files and database records"""
    print("🧹 Starting CSV data cleanup...")
    
    # Clear database records
    csv_count = CSVData.objects.count()
    print(f"📊 Found {csv_count} CSV records in database")
    
    if csv_count > 0:
        # Show what will be deleted
        print("\n📋 Records to be deleted:")
        for csv_data in CSVData.objects.all():
            print(f"  - {csv_data.name} (uploaded: {csv_data.uploaded_at})")
        
        # Clear database
        CSVData.objects.all().delete()
        print(f"✅ Deleted {csv_count} CSV records from database")
    else:
        print("ℹ️  No CSV records found in database")
    
    # Clean CSV files directory
    csv_dir = os.path.join(settings.MEDIA_ROOT, 'csv_files')
    print(f"\n📁 CSV directory: {csv_dir}")
    
    if os.path.exists(csv_dir):
        files_before = os.listdir(csv_dir)
        print(f"📄 Found {len(files_before)} files in CSV directory")
        
        if files_before:
            print("🗑️  Files to be deleted:")
            for filename in files_before:
                print(f"  - {filename}")
        
        # Remove all files
        shutil.rmtree(csv_dir)
        os.makedirs(csv_dir, exist_ok=True)
        print(f"✅ Cleaned {len(files_before)} CSV files")
    else:
        os.makedirs(csv_dir, exist_ok=True)
        print("📁 Created CSV directory")
    
    print("\n🎉 CSV data cleanup completed successfully!")

if __name__ == '__main__':
    clean_csv_data()
