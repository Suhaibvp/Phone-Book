from django.http import HttpResponse
from django.shortcuts import render
# from .models import testtb
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings

from .models import *

def index(request):
    return render(request,'index.html')

def reg(request):
    return render(request,'register.html')

def add(request):
    return render (request,'add.html')

def login(request):
    return render(request,'login.html')

def uregister(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        occupation=request.POST.get('occupation')
        age=request.POST.get('age')
        umob=request.POST.get('umob')
        email=request.POST.get('email')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        pincode=request.POST.get('pincode')
        image=request.FILES['image']
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=FileSystemStorage()
        b=a.save(image.name,image)
        log=userdetailss(fname=fname,lname=lname,image=image,occupation=occupation,umob=umob,age=age,email=email,city=city,state=state,country=country,pincode=pincode,username=username,password=password)
        log.save()
        return redirect('/')
    return render(request,'register.html')


def creg(request):
    if request.method=='POST':
        cname=request.POST.get('cname')
        mob=request.POST.get('mob')
        cemail=request.POST.get('cemail')
        cplace=request.POST.get('cplace')
        image=request.FILES['image']
        a=FileSystemStorage()
        b=a.save(image.name,image)
        log=cadd(cname=cname,mob=mob,cemail=cemail,cplace=cplace,image=image)
        log.save()
        return redirect(cfview)
    return render(request,'add.html')



def cview(request):
    return render(request,'cview.html')

def cfview(request):
    cv=cadd.objects.all()
    return render(request,'cview.html' , {'result':cv})
def rview(request):
    return render(request,'rview.html')

def rfview(request):
    rv=userdetailss.objects.all()
    return render(request,'rview.html',{'result':rv})





def ulogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email)
    print(password)
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logins'] = email
        request.session['admin'] ='admin'
        return render(request,'index.html')

    elif userdetailss.objects.filter(email=email,password=password).exists():
        users=userdetailss.objects.get(email=request.POST['email'],password=password)
        if users.password == request.POST['password']:
            request.session['uid'] = users.id
            request.session['fname'] = users.fname
            request.session['email'] = email
            request.session['asha'] = 'asha'
            return render(request,'index.html')
    # elif userregisters.objects.filter(email=email,password=password).exists():
    #     userdetails=userregisters.objects.get(email=request.POST['email'],password=password)
    #     if userdetails.password == request.POST['password']:
    #         request.session['uid'] = userdetails.id
    #         request.session['uname'] = userdetails.uname

    #         request.session['email'] = email

    #         request.session['user'] = 'user'

            
    #         return render(request,'index.html')


    else:
            return render(request, 'login.html', {'status': 'failed'})



def ulogout(request):
    request.session.delete()
    return redirect('/')








def vprofile(request):
    se=request.session['uid']
    sv=userdetailss.objects.get(id=se)
    return render(request,'uprofile.html',{'result':sv})



def adminview(request):
    return render(request,'aprofile.html')


def cdelete(request,id):
    mark=cadd.objects.get(pk=id)
    mark.delete()
    return redirect(cfview)

def udelete(request,id):
    mark=userdetailss.objects.get(pk=id)
    mark.delete()
    return redirect(rfview)


def cupdate(request,id):
    mark=cadd.objects.get(pk=id)
    return render(request,'cupdate.html',{'res':mark})


def ccupdate(request,id):
    if request.method=='POST':
        cname=request.POST.get('cname')
        mob=request.POST.get('mob')
        cemail=request.POST.get('cemail')
        cplace=request.POST.get('cplace')
        image=request.FILES['image']        
        a=FileSystemStorage()
        b=a.save(image.name,image)
        sub=cadd(cname=cname,mob=mob,cemail=cemail,cplace=cplace,id=id,image=image)
        sub.save()
        return redirect(cfview)


def uupdate(request,id):
    mark=userdetailss.objects.get(pk=id)
    return render(request,'uupdate.html',{'res':mark})


def uuupdate(request,id):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        occupation=request.POST.get('occupation')
        age=request.POST.get('age')
        umob=request.POST.get('umob')
        email=request.POST.get('email')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        pincode=request.POST.get('pincode')
        image=request.FILES['image']
        username=request.POST.get('username')
        password=request.POST.get('password')
        a=FileSystemStorage()
        b=a.save(image.name,image)
        log=userdetailss(fname=fname,lname=lname,occupation=occupation,umob=umob,age=age,email=email,city=city,state=state,country=country,pincode=pincode,username=username,password=password,id=id,image=image)
        log.save()
        return redirect(vprofile)

