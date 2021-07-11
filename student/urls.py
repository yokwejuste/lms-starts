from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('element', views.element),
    path('about', views.about, name='about'),
    path('blog1', views.about, name='blog1'),
    path('blog2', views.about, name='blog2')
]
