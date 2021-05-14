from django.shortcuts import render,HttpResponse
from . models import Register

# Create your views here.
def index(request):
    if request.method=="POST":
        nameOfApplicant = request.POST.get('nameOfApplicant','')
        fatherName = request.POST.get('fatherName','')
        motherName = request.POST.get('motherName','')
        address = request.POST.get('address','')
        zip = request.POST.get('zip','')
        aadhar = request.POST.get('aadhar','')
        pan = request.POST.get('pan','')
        officeName = request.POST.get('officeName','')
        officeAddress = request.POST.get('officeAddress','')
        designation = request.POST.get('designation','')
        bossName = request.POST.get('bossName','')
        experience = request.POST.get('experience','')
        refName = request.POST.get('refName','')
        refContactnum = request.POST.get('refcontactnum','')
        refRelationship = request.POST.get('refrelationship','')
        refAddress = request.POST.get('refaddress','')
        print(nameOfApplicant)
        register=Register(nameOfApplicant=nameOfApplicant,fatherName=fatherName,motherName=motherName,address=address,zip=zip,aadhar=aadhar,pan=pan,officeName=officeName,officeAddress=officeAddress,designation=designation,bossName=bossName,experience=experience,refName=refName,refContactnum=refContactnum,refRelationship=refRelationship,refAddress=refAddress,)
        register.save()
        #return HttpResponse("<script>alert('Data Stored Successfully')</script>")
        return render(request,'userregister/index.html',{'register':register})
    return render(request,'userregister/index.html')
