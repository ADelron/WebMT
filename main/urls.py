from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gallery.html', views.gallery, name="gallery"),
    path('index.html', views.index, name="home"),
    path('aboutus.html', views.aboutus),
    path('registration.html', views.registration, name='register'),
    path('login.html', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('add.html', views.addPhoto),
    path('jafar.html', views.jafar),
    path('askhat.html', views.askhat),
    path('sandu.html', views.sandu),
    path('yernar.html', views.yernar),
    path('nurken.html', views.nurken),
    path('adil.html', views.adil),
    path('akosya.html', views.akosya),
    path('nazerke.html', views.nazerke),
    path('arunaz.html', views.arunaz),
    path('sanzhar.html', views.sanzhar),
    path('balnur.html', views.balnur),
    path('lailym.html', views.lailym),
    path('altyn.html', views.altyn),
    path('nurai.html', views.nurai),
    path('symbat.html', views.symbat),
    path('alua.html', views.alua),
    path('dilya.html', views.dilya),
    path('rabi.html', views.rabiga),
    path('create.html', views.create),
]

