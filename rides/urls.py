from django.urls import path
from .views import calculate_distance_view
from . import views
# from views.login_form

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # path('adminpage/', views.admin, name='adminpage'),
    path('rider/', views.rider, name='rider'),
    path('driver/', views.driver, name='driver'),

    path('', views.home, name='home'),
    path('authentication/', views.authentication, name='authentication'),
    path('changePass/', views.user_change_pass, name="changePass"),
    path('forgotPass/', views.forgotPass, name="forgotPass"),

    path('distance/', calculate_distance_view, name='calaculate-view'),

    path('settings/', views.settings, name="settings"),
]