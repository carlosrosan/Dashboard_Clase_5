import pandas as pd
import json
import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import CSVData
import shutil


def dashboard_view(request):
    """Main dashboard view that displays CSV data as charts"""
    csv_files = CSVData.objects.all()
    
    # Default to first CSV file if available
    csv_data = None
    chart_data = None
    
    if csv_files.exists():
        latest_csv = csv_files.first()
        # Check if file_path is already absolute or relative
        if os.path.isabs(latest_csv.file_path):
            # If it's already an absolute path, use it directly
            csv_path = latest_csv.file_path
        else:
            # If it's relative, join with MEDIA_ROOT
            csv_path = os.path.join(settings.MEDIA_ROOT, latest_csv.file_path)
        
        try:
            # Read CSV data
            df = pd.read_csv(csv_path, low_memory=False)
            
            # Prepare chart data
            chart_data = prepare_chart_data(df)
            
        except Exception as e:
            print(f"Error reading CSV: {e}")
    
    context = {
        'csv_files': csv_files,
        'chart_data': chart_data,
        'csv_data': csv_data,
    }
    
    return render(request, 'dashboard_app/dashboard.html', context)


def upload_csv(request):
    """Handle CSV file upload"""
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        # Save file to media directory
        file_path = default_storage.save(f'csv_files/{csv_file.name}', ContentFile(csv_file.read()))
        
        # Create CSVData record with relative path
        csv_data = CSVData.objects.create(
            name=csv_file.name,
            file_path=file_path  # Store relative path
        )
        
        return redirect('dashboard_app:dashboard')
    
    return render(request, 'dashboard_app/upload.html')


def get_csv_file_path(file_path):
    """Helper function to get the correct CSV file path"""
    # Normalize the path to handle different path separators
    file_path = os.path.normpath(file_path)
    
    # Check if it's already an absolute path
    if os.path.isabs(file_path):
        return file_path
    
    # If it's relative, join with MEDIA_ROOT
    return os.path.join(settings.MEDIA_ROOT, file_path)


def prepare_chart_data(df):
    """Prepare data for various chart types"""
    chart_data = {}
    
    try:
        # Get numeric columns for charts
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        
        # Line chart data (first numeric column over index)
        if numeric_columns:
            chart_data['line_chart'] = {
                'x': list(range(len(df))),
                'y': df[numeric_columns[0]].tolist(),
                'title': f'{numeric_columns[0]} Over Time',
                'x_label': 'Index',
                'y_label': numeric_columns[0]
            }
        
        # Bar chart data (categorical vs numeric)
        if categorical_columns and numeric_columns:
            # Group by first categorical column and sum first numeric column
            grouped = df.groupby(categorical_columns[0])[numeric_columns[0]].sum().reset_index()
            chart_data['bar_chart'] = {
                'x': grouped[categorical_columns[0]].tolist(),
                'y': grouped[numeric_columns[0]].tolist(),
                'title': f'{numeric_columns[0]} by {categorical_columns[0]}',
                'x_label': categorical_columns[0],
                'y_label': numeric_columns[0]
            }
        
        # Pie chart data (categorical distribution)
        if categorical_columns:
            value_counts = df[categorical_columns[0]].value_counts()
            chart_data['pie_chart'] = {
                'labels': value_counts.index.tolist(),
                'values': value_counts.values.tolist(),
                'title': f'Distribution of {categorical_columns[0]}'
            }
        
        # Scatter plot (if we have at least 2 numeric columns)
        if len(numeric_columns) >= 2:
            chart_data['scatter_plot'] = {
                'x': df[numeric_columns[0]].tolist(),
                'y': df[numeric_columns[1]].tolist(),
                'title': f'{numeric_columns[1]} vs {numeric_columns[0]}',
                'x_label': numeric_columns[0],
                'y_label': numeric_columns[1]
            }
        
        # Data table
        chart_data['data_table'] = {
            'columns': df.columns.tolist(),
            'data': df.head(10).values.tolist()  # First 10 rows
        }
        
        # Summary statistics
        chart_data['summary'] = {
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'numeric_columns': numeric_columns,
            'categorical_columns': categorical_columns
        }
        
    except Exception as e:
        print(f"Error preparing chart data: {e}")
        chart_data['error'] = str(e)
    
    return chart_data


def get_chart_data(request, csv_id):
    """API endpoint to get chart data for a specific CSV file"""
    try:
        csv_data = CSVData.objects.get(id=csv_id)
        csv_path = get_csv_file_path(csv_data.file_path)
        df = pd.read_csv(csv_path, low_memory=False)
        chart_data = prepare_chart_data(df)
        return JsonResponse(chart_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def clean_csv_data(request):
    """Clean all CSV files and database records"""
    if request.method == 'POST':
        try:
            print("Clean data request received")  # Debug log
            
            # Clear database records
            csv_count = CSVData.objects.count()
            print(f"Found {csv_count} CSV records to delete")  # Debug log
            CSVData.objects.all().delete()
            
            # Clean CSV files directory
            csv_dir = os.path.join(settings.MEDIA_ROOT, 'csv_files')
            print(f"CSV directory: {csv_dir}")  # Debug log
            
            if os.path.exists(csv_dir):
                # Get list of files before deletion for logging
                files_before = os.listdir(csv_dir)
                print(f"Files to delete: {files_before}")  # Debug log
                
                shutil.rmtree(csv_dir)
                os.makedirs(csv_dir, exist_ok=True)
                print("CSV directory cleaned and recreated")  # Debug log
            else:
                print("CSV directory does not exist")  # Debug log
            
            # Return success response
            return JsonResponse({
                'success': True,
                'message': f'Successfully cleaned {csv_count} CSV files and database records.'
            })
            
        except Exception as e:
            print(f"Error in clean_csv_data: {str(e)}")  # Debug log
            return JsonResponse({
                'success': False,
                'message': f'Error cleaning data: {str(e)}'
            }, status=500)
    
    print("Invalid request method for clean_csv_data")  # Debug log
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)
