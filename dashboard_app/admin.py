from django.contrib import admin
from .models import CSVData


@admin.register(CSVData)
class CSVDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_path', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('name', 'file_path')
