from django.contrib import admin
from django.urls import path
from AcadSecure import views

urlpatterns = [
    path('@krmu_admin', admin.site.urls,name='master'),
    path('', views.index,name='home_blank'),
    path('home/', views.index,name='home'),
    path('about-us/', views.about_us,name='about'),
    path('contact-us/', views.contact_us,name='support'),
    path('login/', views.login,name='login'),
    path('forgot-password/', views.forgot_password,name='password_reset'),
]