from django.db import models

# Create your models here.
class JobSeeker(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key="True")
    dob=models.CharField(max_length=20)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    keyskills=models.TextField()
    regdate=models.CharField(max_length=20)

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)

class Employer(models.Model):
    firmname=models.CharField(max_length=100)
    firmwork=models.TextField()
    firmaddress=models.TextField()
    cpname=models.CharField(max_length=50)
    cpcontactno=models.CharField(max_length=15)
    cpemailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    gstno=models.CharField(max_length=15)
    regdate=models.CharField(max_length=20)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    enquirytext=models.TextField()
    posteddate=models.CharField(max_length=30)

class Jobs(models.Model):
    firmname=models.CharField(max_length=100)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    jobdesc=models.TextField()
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    salarypa=models.IntegerField()
    posteddate=models.CharField(max_length=30)
    emailaddress=models.EmailField(max_length=50)

class AppliedJobs(models.Model):
    empemailaddress=models.EmailField(max_length=50)
    jobtitle=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50, primary_key="True")
    dob=models.CharField(max_length=20)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=20)
    keyskills=models.TextField()
    applieddate=models.CharField(max_length=30)

class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)
