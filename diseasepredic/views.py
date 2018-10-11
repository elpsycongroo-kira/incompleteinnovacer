from django.shortcuts import render
from . import PriaidDiagnosisClientDemo

# from django.http import HttpResponse
def index(request):
    return render(request, 'disease/index.html', {})
# Create your views here.
def disease(request):
    symptoms=request.POST['symptoms']
    print(symptoms)
    diagnosisClientDemo = PriaidDiagnosisClientDemo.PriaidDiagnosisClientDemo()
    diagnosisClientDemo.simulate(symptoms)
    return render(request, 'disease/index.html', {"symptoms":symptoms})