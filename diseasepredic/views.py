from django.shortcuts import render
from . import PriaidDiagnosisClientDemo
from .models import Diseases,Symptoms,combination

# from django.http import HttpResponse
def index(request):
    return render(request, 'disease/index.html', {})
# Create your views here.
def disease(request):
    symptoms=request.POST['symptoms']
    print(symptoms)
    diagnosisClientDemo = PriaidDiagnosisClientDemo.PriaidDiagnosisClientDemo()
    diagnosislist=diagnosisClientDemo.simulate(symptoms)
    lis=[]

    for d in diagnosislist:
        dis = Diseases()
        dis.disease_name=d["Name"]
        dis.disease_description=d["Description"]
        dis.disease_treatment=d["TreatmentDescription"]
        lis.append(dis)
        dis.save()
    return render(request, 'disease/index.html', {"diagnosis":lis})