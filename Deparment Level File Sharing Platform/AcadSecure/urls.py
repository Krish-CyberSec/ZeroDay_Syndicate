from django.contrib import admin
from django.urls import path
from AcadSecure import views

urlpatterns = [
    path('@krmu_admin', admin.site.urls,name='master'),
    path('', views.index,name='home_blank'),
    path('home/', views.index,name='home'),
    path('about-us/', views.about_us,name='about'),
]