from django.shortcuts import render,redirect
from . models import JobSeeker,Login,Employer,Enquiry,Jobs,AppliedJobs,News
import datetime

# Create your views here.
def index(request):
    nw=News.objects.all()
    return render(request,'index.html',{'nw':nw})

def about(request):
    nw=News.objects.all()
    return render(request,'about.html',{'nw':nw})

def jobseekerreg(request):
    nw = News.objects.all()
    return render(request,'jobseekerreg.html',{'nw':nw})

def employerreg(request):
    nw = News.objects.all()
    return render(request,'employerreg.html',{'nw':nw})
def login(request):
    nw = News.objects.all()
    return render(request,'login.html',{'nw':nw})
def contact(request):
    nw = News.objects.all()
    return render(request,'contact.html',{'nw':nw})
def jsreg(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    dob=request.POST['dob']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    keyskills=request.POST['keyskills']
    regdate=datetime.datetime.today()
    password=request.POST['password']
    usertype='jobseeker'
    js=JobSeeker(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,regdate=regdate)
    log=Login(userid=emailaddress,password=password,usertype=usertype)
    js.save()
    log.save()
    msg='Registration is Done successfully'
    return render(request,'jobseekerreg.html',{'msg':msg})

def ereg(request):
    firmname=request.POST['firmname']
    firmwork=request.POST['firmwork']
    firmaddress=request.POST['firmaddress']
    cpname=request.POST['cpname']
    cpcontactno=request.POST['cpcontactno']
    cpemailaddress=request.POST['cpemailaddress']
    aadharno=request.POST['aadharno']
    panno=request.POST['panno']
    gstno=request.POST['gstno']
    regdate=datetime.datetime.today()
    password=request.POST['password']
    usertype='employer'
    e=Employer(firmname=firmname,firmwork=firmwork,firmaddress=firmaddress,cpname=cpname,cpcontactno=cpcontactno,cpemailaddress=cpemailaddress,aadharno=aadharno,panno=panno,gstno=gstno,regdate=regdate)
    log=Login(userid=cpemailaddress,password=password,usertype=usertype)
    e.save()
    log.save()
    msg='Registration is successfull'
    return render(request,'employerreg.html',{'msg':msg})
def saveenq(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    posteddate=datetime.datetime.today()
    enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,posteddate=posteddate)
    enq.save()
    msg='Enquiry is submitted'
    return render(request,'contact.html',{'msg':msg})
def validate(request):
    userid=request.POST['userid']
    password=request.POST['password']
    usertype=request.POST['usertype']
    try:
        obj=Login.objects.get(userid=userid,password=password)
        if obj.usertype=='employer':
            request.session['employer']=userid
            return redirect('emphome')
        elif obj.usertype=='jobseeker':
            request.session['jobseeker']=userid
            return redirect('jobhome')
        elif obj.usertype=='admin':
            request.session['admin']=userid
            return redirect('adminhome')
    except:
        msg='Invalid User'
    return render(request,'login.html',{'msg':msg})

def emphome(request):
    return render(request,'emphome.html')
def postjob(request):
    try:
        if request.session['employer']:
            return render(request,'postjob.html')
    except:
        return render(request,'login.html')

def manageapp(request):
    try:
        if request.session['employer']:
            aj=AppliedJobs.objects.filter(empemailaddress=request.session['employer']).all()
            return render(request,'manageapp.html',{'aj':aj})
    except:
        return render(request,'login.html')
def empchangepassword(request):
    try:
        if request.session['employer']:
            return render(request,'empchangepassword.html')
    except:
        return render(request,'login.html')
def emplogout(request):
    request.session['employer']=None
    return render(request,'login.html')

def pjob(request):
    obj=Employer.objects.get(cpemailaddress=request.session['employer'])
    firmname=obj.firmname
    emailaddress=obj.cpemailaddress
    jobtitle=request.POST['jobtitle']
    post=request.POST['post']
    jobdesc=request.POST['jobdesc']
    qualification=request.POST['qualification']
    experience=request.POST['experience']
    location=request.POST['location']
    salarypa=request.POST['salarypa']
    posteddate=datetime.datetime.today()
    j=Jobs(firmname=firmname,jobtitle=jobtitle,post=post,jobdesc=jobdesc,qualification=qualification,experience=experience,location=location,salarypa=salarypa,posteddate=posteddate,emailaddress=emailaddress)
    j.save()
    msg='Job is posted'
    return render(request,'postjob.html',{'msg':msg})

def empchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg='Message='
    if newpassword!=confirmpassword:
        msg=msg+'Newpassword and Confirmpassword are not equal'
        return render(request,'empchangepassword.html',{'msg':msg})
    userid=request.session['employer']
    usertype='employer'
    try:
        obj=Login.objects.get(userid=userid,password=oldpassword,usertype=usertype)
        log=Login(userid=userid,password=newpassword,usertype=usertype)
        log.save()
        return redirect('emplogout')
    except:
        msg=msg+'Old password is not matched'
    return render(request,'empchangepassword.html',{'msg':msg})

def jobhome(request):
    return render(request,'jobhome.html')

def applyjob(request):
    try:
        if request.session['jobseeker']:
            jb=Jobs.objects.all()
            return render(request,'applyjob.html',{'jb':jb})
    except:
        return render(request,'login.html')

def jobchangepassword(request):
    try:
        if request.session['jobseeker']:
            return render(request,'jobchangepassword.html')
    except:
        return render(request,'login.html')

def joblogout(request):
    request.session['jobseeker']=None
    return render(request,'login.html')

def jobchangepwd(request):
    oldpassword=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    msg='Message='
    if newpassword!=confirmpassword:
        msg=msg+'Newpassword and Confirmpassword are not equal'
        return render(request,'jobchangepassword.html',{'msg':msg})
        userid=request.session['jobseeker']
    try:
        obj=Login.objects.get(userid=userid,password=oldpassword)
        Login.objects.filter(userid=userid).update(password=newpassword)
        return redirect('joblogout')
    except:
        msg=msg+'Old password is not matched'
        return render(request,'jobchangepassword.html',{'msg':msg})

def appliedjobs(request,id):
    obj1=Jobs.objects.get(id=id)
    empemailaddress=obj1.emailaddress
    jobtitle=obj1.jobtitle
    post=obj1.post
    obj2=JobSeeker.objects.get(emailaddress=request.session['jobseeker'])
    name=obj2.name
    gender=obj2.gender
    address=obj2.address
    contactno=obj2.contactno
    emailaddress=obj2.emailaddress
    dob=obj2.dob
    qualification=obj2.qualification
    experience=obj2.experience
    keyskills=obj2.keyskills
    applieddate=datetime.datetime.today()
    aj=AppliedJobs(empemailaddress=empemailaddress,jobtitle=jobtitle,post=post,name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,dob=dob,qualification=qualification,experience=experience,keyskills=keyskills,applieddate=applieddate)
    aj.save()
    return redirect('jobhome')

def jsprofile(request,id):
    obj=AppliedJobs.objects.get(id=id)
    return render(request,'jsprofile.html',{'obj':obj})

def adminhome(request):
    nw=News.objects.all()
    return render(request,'adminhome.html',{'nw':nw})

def enquiries(request):
    try:
        if request.session['admin']:
            enq=Enquiry.objects.all()
            return render(request,'enquiries.html',{'enq':enq})
    except:
        return render(request,'login.html')

def jobseekers(request):
    try:
        if request.session['admin']:
            js=JobSeeker.objects.all()
            return render(request,'jobseekers.html',{'js':js})
    except:
        return render(request,'login.html')

def employers(request):
    try:
        if request.session['admin']:
            emp=Employer.objects.all()
            return render(request,'employers.html',{'emp':emp})
    except:
        return render(request,'login.html')

def adminlogout(request):
    request.session['admin']=None
    return render(request,'login.html')

def addnews(request):
    newstext=request.POST['newstext']
    newsdate=datetime.datetime.today()
    nw=News(newstext=newstext,newsdate=newsdate)
    nw.save()
    return redirect('adminhome')
def deletenews(request,id):
    obj=News.objects.get(id=id)
    obj.delete()
    return redirect('adminhome')
