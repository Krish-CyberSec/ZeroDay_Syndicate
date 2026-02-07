from django.shortcuts import render

# Create your views here.
def notifications_list(request):
    return render(request, 'notifications/notifications_list.html')