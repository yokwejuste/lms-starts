import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def index(request):
    today = datetime.datetime.now().date()
    return render(request, 'index.html', {"today": today})


def about(request):
    return render(request, 'about.html')


def element(request):
    return render(request, 'elements.html')


def courses(request):
    return render(request, 'courses.html')


def detail(request):
    return render(request, 'course-details.html')


def contact(request):
    return render(request, 'contacts.html')


def blog1(request):
    return render(request, 'blog-single.html')


def blog2(request):
    return render(request, 'blog-home.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def login1(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')
