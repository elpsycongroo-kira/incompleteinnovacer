from django.shortcuts import render
from . import PriaidDiagnosisClientDemo
from django.core.exceptions import ObjectDoesNotExist
from .models import Diseases,Symptoms,combination

# from django.http import HttpResponse
def index(request):
    """ This function returns the rendered symptoms page of the website. """
    return render(request, 'disease/index.html', {})
# Create your views here.
def disease(request):
    """ This function returns the rendered diseases page of the website.

        The formdata contains the symptoms entered by the user, after splitting the symptoms,we loop through the symptoms, if
        it is not there in the database we go through the api checking the diseases for the symptom and enter them in database,
        if the symptom is already there in database we get it's corresponding saved diseases from combination table. Then we
        take the common diseases of all the lists of symptoms.
    """
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
