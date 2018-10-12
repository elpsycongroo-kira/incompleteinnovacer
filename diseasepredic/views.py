from django.shortcuts import render
from . import PriaidDiagnosisClientDemo
from django.core.exceptions import ObjectDoesNotExist
from .models import Diseases,Symptoms,combination

# from django.http import HttpResponse
def index(request):
    return render(request, 'disease/index.html', {})
# Create your views here.
def disease(request):
    formdata=request.POST['symptoms']
    formdata=formdata.split(",")
    # print(formdata)
    mainlis=[]
    for symptoms in formdata:
        lis = []
        try:
            symptom=Symptoms.objects.get(symptom_name=symptoms.lower())
            com = combination.objects.filter(symptomid=symptom)
            for i in com:
                lis.append(i.diseaseid)
        except ObjectDoesNotExist:
            print("came here")
            symptom=Symptoms()
            symptom.symptom_name=symptoms.lower()
            symptom.save()
            diagnosisClientDemo = PriaidDiagnosisClientDemo.PriaidDiagnosisClientDemo()
            diagnosislist=diagnosisClientDemo.simulate(symptoms)
            for d in diagnosislist:
                com=combination()
                try:
                    dis = Diseases.objects.get(disease_name=d["Name"])
                except ObjectDoesNotExist:
                    dis = Diseases()
                    dis.disease_name=d["Name"]
                    dis.disease_description=d["Description"]
                    dis.disease_treatment=d["TreatmentDescription"]
                    dis.save()
                lis.append(dis)
                com.diseaseid = dis
                com.symptomid = symptom
                com.name=dis.disease_name+symptom.symptom_name
                com.save()
        if not mainlis:
            mainlis=lis
        mainlis=list(set(mainlis) & set(lis))
        # print(mainlis)

    return render(request, 'disease/index.html', {"diagnosis":mainlis})