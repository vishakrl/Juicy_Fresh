from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def test(r):
    return render(r,'test.html',{'val':'java'})

def loginpage(r):
    return render(r,'login.html')

def registerpage(r):
    return render(r,'register.html')

def loginsub(request):
    uname = request.POST['uname']
    pword = request.POST['pword']
    user = auth.authenticate(username=uname,password=pword)
    if user:
        auth.login(request,user)
        return redirect('/')
    return render(request,'test.html',{'val':uname})

def registersub(request):
    uname = request.POST['uname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pword = request.POST['pword']
    rpword = request.POST['rpword']
    if pword==rpword:
        if User.objects.filter(username=uname):
            msg="username is already taken"
            return render(request,'test.html',{'val':msg})
        elif User.objects.filter(email=email):
            msg="email is already taken"
            return render(request,'test.html',{'val':msg})
        
        else:
          user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pword)
          user.save();
          return redirect("/")
         
    else:
         msg="invalid password"
    

         return render(request,'test.html',{'val':msg})