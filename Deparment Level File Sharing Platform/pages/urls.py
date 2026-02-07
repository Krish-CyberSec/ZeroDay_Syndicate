from django.urls import path
from . import views

urlpatterns = [

    # Public pages
    path('', views.index, name='home_blank'),
    path('home/', views.index, name='home'),
    path('about-us/', views.about_us, name='about'),
    path('contact-us/', views.contact_us, name='support'),

    # Dashboards
    path('student-dashboard/', views.student_dashboard,
         name='student_dashboard'),

    path('faculty-dashboard/', views.faculty_dashboard,
         name='faculty_dashboard'),

    path('admin-dashboard/', views.admin_dashboard,
         name='admin_dashboard'),
]
