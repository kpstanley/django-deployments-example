from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'basicapp/form_page.html')
