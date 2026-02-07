from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# ---------- Public Pages ----------

def index(request):
    return render(request, 'pages/index.html')


def about_us(request):
    return render(request, 'pages/about.html')


def contact_us(request):
    return render(request, 'pages/support.html')


# ---------- Dashboards ----------

@login_required
def student_dashboard(request):
    return render(request, 'pages/student_dashboard.html')


@login_required
def faculty_dashboard(request):
    return render(request, 'pages/faculty_dashboard.html')


@login_required
def admin_dashboard(request):
    return render(request, 'pages/admin_dashboard.html')
