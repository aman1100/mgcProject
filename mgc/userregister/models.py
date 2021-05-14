from django.db import models

# Create your models here.
class Register(models.Model):
    nameOfApplicant=models.CharField(max_length=50,default="")
    fatherName=models.CharField(max_length=50,default="")
    motherName=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")
    zip=models.CharField(max_length=50,default="")
    aadhar=models.CharField(max_length=50,primary_key=True)
    pan=models.CharField(max_length=50,default="")
    officeName=models.CharField(max_length=50,default="")
    officeAddress=models.CharField(max_length=50,default="")
    designation=models.CharField(max_length=50,default="")
    bossName=models.CharField(max_length=50,default="")
    experience=models.CharField(max_length=50,default="")
    refName=models.CharField(max_length=50,default="")
    refContactnum=models.CharField(max_length=50,default="")
    refRelationship=models.CharField(max_length=50,default="")
    refAddress=models.CharField(max_length=50,default="")

    def __str__(self):
        return self.nameOfApplicant