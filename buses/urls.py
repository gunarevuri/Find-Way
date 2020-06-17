from django.contrib import admin
from django.urls import path,include
from .views import displaybuses,findLocation, signupuser, userloginview, userauthenticate,userlogout, homepageview


urlpatterns = [
    path('bus/<int:id>/',displaybuses,name='displaybuses'),
    path('fetchlocation/',findLocation,name='location'),

    path('',homepageview,name='homepageview'),
    path('signupuser/', signupuser, name="signupuser"),
	path('loginuser/', userloginview, name = 'userloginview'),
	path('userauthenticate/', userauthenticate, name= 'userauthenticate'),
	path('userlogout/', userlogout, name='userlogout'),
]
