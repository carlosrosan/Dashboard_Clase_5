from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('clean/', views.clean_csv_data, name='clean_csv_data'),
    path('api/latest-data/', views.get_latest_data, name='latest_data'),
    path('api/set-source/', views.set_csv_source, name='set_csv_source'),
    path('api/chart-data/<int:csv_id>/', views.get_chart_data, name='chart_data'),
]
