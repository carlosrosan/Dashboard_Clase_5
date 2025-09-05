from django.urls import path
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('clean/', views.clean_csv_data, name='clean_csv_data'),
]
