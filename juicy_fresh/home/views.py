from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import fruits 

# Create your views here.

def index(request):
    obj=fruits.objects.all()
    if 'username' in request.COOKIES:

        u=request.COOKIES['username']
    else:
        u=''
    print('hai',obj)
    return render(request,"index.html",{'data':obj,'name':u})



def test(r):
    return render(r,'test.html',{'val':'java'})



def login(request):
        if request.method=="POST":
        
            uname = request.POST['uname']
            pword = request.POST['pword']
            user = auth.authenticate(username=uname,password=pword)
            if user:
                
                auth.login(request,user)
                res=redirect('/')
                res.set_cookie("username",uname)
                return res
            msg="invalid user name and password"
            return render(request,'login.html',{'msg':msg})
        else:
            return render(request,'login.html')


def register(request):
    if request.method=="POST":
        
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pword = request.POST['pword']
        rpword = request.POST['rpword']
        if pword==rpword:
            if User.objects.filter(username=uname):
                msg="username is already taken"
                return render(request,'register.html',{'val':msg})
            elif User.objects.filter(email=email):
                msg="email is already taken"
                return render(request,'register.html',{'val':msg})
            
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pword) 
                user.save();
                auth.login(request,user) 
                return redirect("/")
                
        else:
            msg="invalid password"
            return render(request,'register.html',{'val':msg})
    else:
        return render(request,"register.html") 


def logout(request):
    auth.logout(request)
    lg= redirect('/')
    lg.delete_cookie('username')
    return lg


def feed(request):
    return render(request,'text.html')

def search(request):
    return render(request,'search.html')

def schsub(request):
    schitem=request.GET['item']
    return render(request,'text.html',{'serh':schitem})