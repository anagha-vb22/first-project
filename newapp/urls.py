from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('display/',display),
    path('uprofile/',uprofile),
    path('sregister/',sregister),
    path('slogin/',slogin),
    path('sprofile/',sprofile),
    path('upload/',imgupload),
    path('imgdis/',imgdisplay),
    path('delete/<int:id>',productdelete),
    path('edit/<int:id>',editproduct),
    path('creg/',creg),
    path('clogin/',clogin),
    path('verify/<auth_token>',verify),
    path('addtocart/<int:id>',addtocart),
    path('cartdisplay/',cartdisplay),
    path('cartdelete/<int:id>',cartdelete),
    path('addtowishlist/<int:id>',addtowishlist),
    path('wishlistdisplay/',wishlistdisplay),
    path('productdisplay/',productdisplay),
    path('wishdelete/<int:id>',wishdelete),
    path('cartbuy/<int:id>',cartbuy),
    path('cardpayment/',cardpayment),
    path('orderstatus/',orderstatus)


]