from django.db import models

class Symptoms(models.Model):
    symptom_name = models.CharField(max_length=250)
    def __str__(self):
        return self.symptom_name

class Diseases(models.Model):
    disease_name = models.CharField(max_length=250)
    disease_description=models.CharField(max_length=1200)
    disease_treatment = models.CharField(max_length=1200)
    def __str__(self):
        return self.disease_name
class combination:
    symptomid=models.ForeignKey(Symptoms,on_delete=models.CASCADE)
    diseaseid=models.ForeignKey(Diseases,on_delete=models.CASCADE)
    def __str__(self):
        return self.symptomid+" "+self.diseaseid
