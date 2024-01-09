
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
import pandas as pd

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file, engine='openpyxl')
            # Process the DataFrame as needed
            return render(request, 'excel_app/display.html', {'df': df})
    else:
        form = ExcelUploadForm()
    return render(request, 'excel_app/upload.html', {'form': form})
