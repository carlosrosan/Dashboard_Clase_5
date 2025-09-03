from django.db import models


class CSVData(models.Model):
    """Model to store CSV data for the dashboard"""
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "CSV Data"
        verbose_name_plural = "CSV Data"
    
    def __str__(self):
        return self.name
