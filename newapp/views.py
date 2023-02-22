from django.contrib.auth import authenticate
from django.core.mail import send_mail
from firstproject.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
import os
import uuid


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data["email"]
            ps = a.cleaned_data["password"]
            b = regmodel.objects.all()
            for i in b:
                if em == i.email and ps == i.password:
                    return redirect(profile)
            else:
                return HttpResponse("Login failed")
    return render(request, 'user login.html')


def display(request):
    a = regmodel.objects.all()
    return render(request, 'display.html', {'a': a})


def slogin(request):
    if request.method == 'POST':
        a = slogform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data["name"]
            em = a.cleaned_data["email"]
            ps = a.cleaned_data["password"]
            request.session['shopname']=nm
            b = sregmodel.objects.all()
            for i in b:
                if nm==i.name and em == i.email and ps == i.password:
                    request.session['id']=i.id
                    return redirect(sprofile)
            else:
                return HttpResponse("Login failed")
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["name"]
            em = a.cleaned_data["email"]
            ph = a.cleaned_data["phone"]
            pin = a.cleaned_data["pincode"]
            ad = a.cleaned_data["address"]
            pa = a.cleaned_data["password"]
            cp = a.cleaned_data["confirm_password"]
            if pa == cp:
                b = regmodel(name=nm, email=em, phone=ph, pincode=pin, address=ad, password=pa)
                b.save()
                return redirect(login)
        else:
            return HttpResponse("Incorrect password")

    return render(request, 'user register.html')


def sregister(request):
    if request.method == 'POST':
        a = shopform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["name"]
            em = a.cleaned_data["email"]
            ph = a.cleaned_data["phone"]
            pin = a.cleaned_data["pincode"]
            ad = a.cleaned_data["address"]
            pa = a.cleaned_data["password"]
            cp = a.cleaned_data["confirm_password"]
            if pa == cp:
                b = sregmodel(name=nm, email=em, phone=ph, pincode=pin, address=ad, password=pa)
                b.save()
                return redirect(slogin)
        else:
            return HttpResponse("Incorrect password")

    return render(request, 'shop register.html')

def uprofile(request):
    a=request.session['username']
    return render(request,'customer profile.html',{'a':a})



def imgdisplay(request):
    shopid=request.session['id']
    a = imgmodel.objects.all()
    name = []
    price1 = []
    description1 = []
    image = []
    id = []
    shopid=[]
    for i in a:
        sid=i.shopid
        shopid.append(sid)
        id1 = i.id
        id.append(id1)
        inm = i.imgname
        name.append(inm)
        pr = i.price
        price1.append(pr)
        de = i.description
        description1.append(de)
        fi = i.imgfile
        image.append(str(fi).split('/')[-1])
    mylist = zip(name, price1, description1, image, id,shopid)
    return render(request, 'imgdisplay.html', {'mylist': mylist,'shopid':shopid})


def sprofile(request):

    name=request.session['shopname']
    return render(request, 'shop profile.html',{'shopname':name})






def imgupload(request):
    if request.method == 'POST':
        a = imgforms(request.POST, request.FILES)
        id=request.session['id']
        if a.is_valid():
            inm = a.cleaned_data["imgname"]
            pr = a.cleaned_data["price"]
            de = a.cleaned_data["description"]
            fi = a.cleaned_data["imgfile"]
            b = imgmodel(shopid=id,imgname=inm, price=pr, description=de, imgfile=fi)
            b.save()
            return redirect(imgdisplay)
        else:
            return HttpResponse("IMAGE UPLOAD FAILED")
    return render(request,'imgupload.html')




def productdelete(request,id):
    a = imgmodel.objects.get(id=id)
    a.delete()
    return redirect(imgdisplay)


def editproduct(request, id):
    a = imgmodel.objects.get(id=id)
    fi = str(a.imgfile).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES):
            if len(a.imgfile) > 0:
                os.remove(a.imgfile.path)
            a.imgfile = request.FILES('imgfile')
        a.imgname = request.POST.get('imgname')
        a.price = request.POST.get('price')
        a.description = request.POST.get('description')
        a.save()
        return redirect(imgdisplay)
    return render(request, 'editproduct.html', {'a': a, 'fi': fi})


def creg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request, 'username already taken')
            return redirect(creg)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already exist')
            return redirect(creg)
        user_obj = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user_obj.set_password(password)
        user_obj.save()

        auth_token = str(uuid.uuid4())
        profile_obj = profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email, auth_token)
        return render(request, 'success.html')
    return render(request, 'customer register.html')


def clogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session["username"]=username
        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect(clogin)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'Profile not verified check your mail')
            return redirect(clogin)
        user = authenticate(username=username, password=password)
        # user=valid
        # if the given credentials are valid,return a user object.
        if user is None:
            messages.success(request, 'Wrong password or username')
            return redirect(clogin)
        return redirect(uprofile)
        # return HttpResponse("Success")
    return render(request, 'customer login.html')


def send_mail_regis(email, auth_token):
    subject = "your account has been verified"
    message = f'click the link to verify your account http://127.0.0.1:8000/newapp/verify/{auth_token}'
    email_from = EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)


def verify(request, auth_token):
    profile_obj = profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request, 'Your account is already verified')
            return redirect(clogin)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request, 'Your account has been verified')
        return redirect(clogin)
    else:
        messages.success(request, 'User not found')
        return redirect(clogin)
def addtocart(request,id):
    a=imgmodel.objects.get(id=id)
    b=cart(imgname=a.imgname,prize=a.price,description=a.description,imgfile=a.imgfile)
    b.save()
    # return HttpResponse("Item added Successfully")
    # return render(request,'add to cart.html')
    return redirect(cartdisplay)

def cartdisplay(request):
    a = cart.objects.all()
    name = []
    price1 = []
    description1 = []
    image = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        fi = i.imgfile
        image.append(str(fi).split('/')[-1])
        inm = i.imgname
        name.append(inm)
        pr = i.prize
        price1.append(pr)
        de = i.description
        description1.append(de)
    mylist = zip(image, name, price1, description1, id)
    return render(request, 'cart.html', {'mylist': mylist})


def cartdelete(request,id):
    a = cart.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)

def cartbuy(request,id):
    a=cart.objects.get(id=id)
    fi=str(a.imgfile).split('/')[-1]
    if request.method=='POST':
        imgname=request.POST.get('imgname')
        de=request.POST.get('description')
        quantity1=request.POST.get('quantity')
        pr=request.POST.get('price')
        b=buy(imgname=imgname,description=de,quantity=quantity1,price=pr)
        b.save()
        total=int(pr)*int(quantity1)
        return render(request,'finalbill.html',{'total':total,'imgname':imgname,'quantity':quantity1})
    return render(request,'quantity.html',{'a':a})


def addtowishlist(request,id):
    a=imgmodel.objects.get(id=id)
    b=wishlist(imgname=a.imgname,price=a.price,description=a.description,imgfile=a.imgfile)
    b.save()
    return redirect(wishlistdisplay)
    # return render(request,'wishlist.html')

def wishlistdisplay(request):
    a = wishlist.objects.all()
    name = []
    price1 = []
    description1 = []
    image = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        fi = i.imgfile
        image.append(str(fi).split('/')[-1])
        inm = i.imgname
        name.append(inm)
        pr = i.price
        price1.append(pr)
        de = i.description
        description1.append(de)
    mylist = zip(image, name, price1, description1, id)
    return render(request, 'wishlist.html', {'mylist': mylist})

def productdisplay(request):
    a = imgmodel.objects.all()
    name = []
    price1 = []
    description1 = []
    image = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        inm = i.imgname
        name.append(inm)
        pr = i.price
        price1.append(pr)
        de = i.description
        description1.append(de)
        fi = i.imgfile
        image.append(str(fi).split('/')[-1])
    mylist = zip(name, price1, description1, image, id)
    return render(request, 'product display.html', {'mylist': mylist})


def wishdelete(request,id):
    a = wishlist.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)


def cardpayment(request):
    if request.method=='POST':
        cardname=request.POST.get('cardname')
        cardnumber= request.POST.get('cardnumber')
        cardexpiry= request.POST.get('cardexpiry')
        securitycode= request.POST.get('securitycode')
        user_obj=customercard(cardname=cardname,cardnumber=cardnumber,cardexpiry=cardexpiry,securitycode=securitycode)
        user_obj.save()
        # a=datetime.date.today()
        # b=a+timedelta(15)
        # print(b)
        return redirect(orderstatus)
    return render(request,'card payment.html')

def orderstatus(request):
    return render(request,'order status.html')