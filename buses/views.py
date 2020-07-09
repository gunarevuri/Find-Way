from django.shortcuts import render,get_object_or_404
from .models import Timings,BusStation
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .forms import FindLocationForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def displaybuses(request,id):

	if not request.user.is_authenticated:
		return redirect(userloginview)
	queryset=Timings.objects.filter(bus_station_id=id)
	# .filter(arrival_time__lte=timezone.localtime(timezone.now()))
	return render(request,'buses/bus_view.html',{'form':queryset})


def findLocation(request):
       
	if not request.user.is_authenticated:
		return redirect(userloginview)
	form=FindLocationForm()
	if request.method=="POST":

		form=FindLocationForm(request.POST or None)
		if form.is_valid():
			latitude=form.cleaned_data['latitude']
			longitude=form.cleaned_data['longitude']
			pnt=Point(latitude,longitude,srid=4328)
			queryset=BusStation.objects.annotate(distance=Distance('location', pnt)).order_by('distance')
			return render(request,'buses/location.html',{'form':queryset})
	return render(request,'buses/home.html',{'form':form})


def homepageview(request):
	context = {
	'username':request.user.username

	}
	return render(request, "buses/homepageview.html",context)

def signupuser(request):
	username = request.POST['username']
	password = request.POST['password']


	# if username already exist 
	if User.objects.filter(username = username).exists():
		messages.add_message(request, messages.ERROR, "user already exist")
		return redirect(homepageview)


	# if username doesnt exist already
	else:
		User.objects.create_user(username = username, password = password).save()
		messages.add_message(request, messages.ERROR, "user created , Login to Find way to your Destination")
		return redirect(homepageview)

def userloginview(request):
	return render(request, 'buses/userlogin.html')

def userauthenticate(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)
	if user is not None:
		login(request, user)
		return redirect(findLocation)

	if user is None:
		messages.add_message(request, messages.ERROR, "username or password is not correct")
		return redirect(userloginview)
# user login view
def userlogout(request):
	if not request.user.is_authenticated:
		return redirect(userloginview)
	logout(request)
	return redirect(userloginview)