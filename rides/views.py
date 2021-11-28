from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# location and destination

from .models import Measurement
from .forms import MeasurementModelForm
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

# Create your views here.

from .models import *
# from .forms import RiderForm, CreateUserForm
from .forms import SignUpForm, LoginForm

def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    #     form = SignUpForm()
    #
    #     if request.method == 'POST':
    #         form = SignUpForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             user = form.cleaned_data.get('username')
    #             messages.success(request, 'Account was created for ' + user)
    #             return redirect('login')
    #
    #     context = {'form':form}
    #     return render(request, 'form.html', context)




    # msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # msg = 'user created'
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            # msg = 'form is not valid'
            messages.success(request, 'Account was not created')
    else:
        form = SignUpForm()
    return render(request,'form.html', {'form': form})

# def register(request):
#     msg = None
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             msg = 'user created'
#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = SignUpForm()
#     return render(request,'register.html', {'form': form, 'msg': msg})

def loginPage(request):
    # form = AuthenticationForm()
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
        # form = AuthenticationForm(request.POST)
        # if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            # form.save()
            user = authenticate(request, username=username, password=password)

            # if user is not None and user.is_admin:
            #     login(request, user)
            #     messages.success(request, 'You login successfully!!! ')
            #     return redirect('home')
            if user is not None and user.is_rider:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')
            elif user is not None and user.is_driver:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {'form':form}
        return render(request, 'form.html', context)


def logoutUser(request):
    logout(request)
    return redirect('logout')

@login_required(login_url='login')
def authentication(request):
    return render(request, "form.html")

@login_required(login_url='login')
def home(request):
    # rider = Riders.objects.all()
    context = {'rider':rider}
    return render(request, "home.html", context)

# def form_sub(request):
#     username = request.POST['username']
#     phone = request.POST['phone']
#     email = request.POST['email']
#     password1 = request.POST['password1']
#     password2 = request.POST['password2']
#
#     form = Riders.objects.create(username=username,
#                                  phone=phone,
#                                  email=email,
#                                  password1=password1,
#                                  password2=password2)
#     form.save()
#     return render(request, "home.html")


# def signup_form(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             form.save()
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     context = {
#         'form': form
#     }
#     return render(request, 'authentication.html', context)
#
# def login_form(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     context = {
#         'form': form
#     }
#     return render(request, 'home.html', context)

@login_required(login_url='login')
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            current = request.POST["cpwd"]
            new_pas = request.POST["npwd"]

            user = User.objects.get(id=request.user.id)
            # un = user.username
            # check = user.check_password(current)
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Update Password successfully!!! ')
                return redirect('home')
        else:
            fm = PasswordChangeForm(user=request.user)
            context = {'form':fm}
            return render(request, "passwordChange.html", context)
    else:
        return redirect('login')


# def change_password(request):
#     context = {}
#     ch = user.objects.filter(user__id=request.user.id)
#     if len(ch) > 0:
#         data = register_table.objects.get(user__id=request.user.id)
#         context["data"] = data
#     if request.method == "POST":
#         current = request.POST["cpwd"]
#         new_pas = request.POST["npwd"]
#
#         user = user.objects.get(id=request.user.id)
#         un = user.username
#         check = user.check_password(current)
#         if check == True:
#             user.set_password(new_pas)
#             user.save()
#             context["msz"] = "Password Changed Successfully!!!"
#             context["col"] = "alert-success"
#             user = User.objects.get(username=un)
#             login(request, user)
#         else:
#             context["msz"] = "Incorrect Current Password"
#             context["col"] = "alert-danger"
#
#     return render(request, "passwordChange.html", context)

def forgotPass(request):
    context = {}
    if request.method == "POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return redirect("/admin")
        else:
            return redirect("home")
        # context["status"] = "Password Changed Successfully!!!"

    return render(request,"Forget_Password.html",context)
#
# def admin(request):
#     return render(request,'home.html')


def rider(request):
    return render(request,'home.html')


def driver(request):
    return render(request,'home.html')

def calculate_distance_view(request):
    # initial values
    distance = None
    destination = None

    obj = get_object_or_404(Measurement, id=1)
    form = MeasurementModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='measurements')

    ip_ = get_ip_address(request)
    # print(ip_)
    # ip = '72.14.207.99'
    country, city, lat, lon = get_geo(ip)
    location = geolocator.geocode(city)

    # location coordinates
    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # initial folium map
    m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon), zoom_start=8)

    # location marker
    folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                  icon=folium.Icon(color='purple')).add_to(m)

    if form.is_valid():
        instance = form.save(commit=False)
        destination_ = form.cleaned_data.get('destination')
        destination = geolocator.geocode(destination_)

        # destination coordinates
        d_lat = destination.latitude
        d_lon = destination.longitude
        pointB = (d_lat, d_lon)
        # distance calculation
        distance = round(geodesic(pointA, pointB).km, 2)

        # folium map modification
        m = folium.Map(width=800, height=500, location=get_center_coordinates(l_lat, l_lon, d_lat, d_lon),
                       zoom_start=get_zoom(distance))
        # location marker
        folium.Marker([l_lat, l_lon], tooltip='click here for more', popup=city['city'],
                      icon=folium.Icon(color='purple')).add_to(m)
        # destination marker
        folium.Marker([d_lat, d_lon], tooltip='click here for more', popup=destination,
                      icon=folium.Icon(color='red', icon='cloud')).add_to(m)

        # draw the line between location and destination
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    m = m._repr_html_()

    context = {
        'distance': distance,
        'destination': destination,
        'form': form,
        'map': m,
    }

    return render(request, 'home.html', context)

def settings(request):
    return render(request, "settings.html")

