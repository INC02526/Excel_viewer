# excel_app/forms.py
from django import forms
from .models import ExcelData

class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelData
        fields = ['file']
