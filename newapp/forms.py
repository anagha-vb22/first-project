from django import forms
class regform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=50)
    pincode=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)
class logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)


class shopform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=50)
    pincode=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)
class slogform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class imgforms(forms.Form):
    imgname=forms.CharField(max_length=300)
    price=forms.IntegerField()
    description=forms.CharField(max_length=30)
    imgfile=forms.ImageField()

class customercardpay(forms.Form):
    cardname=forms.CharField(max_length=30)
    cardnumber=forms.CharField(max_length=30)
    cardexpiry=forms.CharField(max_length=30)
    securitycode=forms.CharField(max_length=30)