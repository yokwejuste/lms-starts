from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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


def base_student(request):
    return render(request, 'student/partials/base_student.html')
