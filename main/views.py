from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Photo
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'main/Web/index.html')


def gallery(request):
    photos = Photo.objects.all()

    context = {'photos': photos}
    return render(request, 'main/Web/gallery.html', context)


def aboutus(request):
    error = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'ERROR'

    form = FeedBackForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/Web/aboutus.html', context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()

        form = UserCreationForm()
        context = {
            "form": form,
        }
        return render(request, 'main/Web/registration.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'main/Web/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        photo = Photo.objects.create(
            image=image,
        )
        return redirect('gallery')

    return render(request, 'main/Web/add.html')


def jafar(request):
    return render(request, 'main/Web/jafar.html')


def askhat(request):
    return render(request, 'main/Web/askhat.html')


def sandu(request):
    return render(request, 'main/Web/sandu.html')


def yernar(request):
    return render(request, 'main/Web/yernar.html')


def nurken(request):
    return render(request, 'main/Web/nurken.html')


def adil(request):
    return render(request, 'main/Web/adil.html')


def akosya(request):
    return render(request, 'main/Web/akosya.html')


def nazerke(request):
    return render(request, 'main/Web/nazerke.html')


def arunaz(request):
    return render(request, 'main/Web/arunaz.html')


def sanzhar(request):
    return render(request, 'main/Web/sanzhar.html')


def balnur(request):
    return render(request, 'main/Web/balnur.html')


def lailym(request):
    return render(request, 'main/Web/lailym.html')


def altyn(request):
    return render(request, 'main/Web/altyn.html')


def nurai(request):
    return render(request, 'main/Web/nurai.html')


def symbat(request):
    return render(request, 'main/Web/symbat.html')


def alua(request):
    return render(request, 'main/Web/alua.html')


def dilya(request):
    return render(request, 'main/Web/dilya.html')


def rabiga(request):
    return render(request, 'main/Web/rabi.html')


def create(request):
    form = FeedBackForm()
    context = {
        "form": form
    }
    return render(request, 'main/Web/create.html', context)
