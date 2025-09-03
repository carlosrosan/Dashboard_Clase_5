# CSV Dashboard Django Project

A Django web application that creates interactive dashboards from CSV data files. The dashboard automatically generates various chart types including line charts, bar charts, pie charts, and scatter plots based on the data structure.

## Features

- **CSV File Upload**: Upload CSV files through a web interface
- **Automatic Chart Generation**: Creates multiple chart types based on data structure:
  - Line charts for time series data
  - Bar charts for categorical vs numeric data
  - Pie charts for categorical distributions
  - Scatter plots for numeric correlations
- **Data Summary**: Shows statistics about the uploaded data
- **Data Preview**: Displays the first 10 rows of data in a table
- **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   - Main dashboard: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

1. **Upload a CSV file**:
   - Click "Upload New CSV" on the dashboard
   - Select a CSV file from your computer
   - Click "Upload CSV"

2. **View the dashboard**:
   - The dashboard will automatically display charts based on your data
   - Different chart types will appear depending on your data structure

3. **Sample data**:
   - Use the included `sample_data.csv` file to test the application

## CSV File Requirements

- File must be in CSV format (.csv)
- First row should contain column headers
- Include both numeric and categorical data for best visualization
- Maximum file size: 10MB

## Sample Data Format

```csv
Name,Age,Department,Salary,Experience,Performance_Score
John Doe,30,Engineering,75000,5,85
Jane Smith,28,Marketing,65000,3,78
...
```

## Project Structure

```
dashboard_project/
├── dashboard_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── dashboard_app/              # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                  # HTML templates
│   ├── base.html
│   └── dashboard_app/
│       ├── dashboard.html
│       └── upload.html
├── manage.py
├── requirements.txt
├── sample_data.csv
└── README.md
```

## Technologies Used

- **Django 4.2.7**: Web framework
- **Pandas**: Data processing and analysis
- **Chart.js**: Interactive charts and graphs
- **Bootstrap 5**: Responsive UI framework
- **SQLite**: Database (default)

## Customization

You can customize the dashboard by:

1. **Adding new chart types** in `dashboard_app/views.py`
2. **Modifying the UI** in the template files
3. **Adding data processing logic** in the `prepare_chart_data` function
4. **Styling** by modifying the CSS in `templates/base.html`

## Troubleshooting

- **CSV upload issues**: Ensure the file is in proper CSV format with headers
- **Charts not displaying**: Check browser console for JavaScript errors
- **Database errors**: Run migrations with `python manage.py migrate`

## License

This project is open source and available under the MIT License.
