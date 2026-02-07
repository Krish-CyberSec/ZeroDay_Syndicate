from django.urls import path
from . import views
app_name = 'accounts'   # IMPORTANT
urlpatterns = [

    path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),

    path('forgot-password/',
         views.forgot_password,
         name='password_reset'),

    path('profile/', views.profile_view, name='profile'),
]
