from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from .models import UserProfile


# # ---------- Login ----------

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            # Fetch role from UserProfile
            profile = UserProfile.objects.get(user=user)

            if profile.role == "ADMIN":
                return redirect("admin_dashboard")

            elif profile.role == "FACULTY":
                return redirect("faculty_dashboard")

            elif profile.role == "STUDENT":
                return redirect("student_dashboard")

        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid username or password"}
            )

    return render(request, "accounts/login.html")


# # ---------- Logout ----------

# def logout_view(request):
#     logout(request)
#     return redirect("login")


# ---------- Forgot Password Page ----------

def forgot_password(request):
    return render(request, "accounts/forgot_password.html")


# ---------- Profile ----------

@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")
