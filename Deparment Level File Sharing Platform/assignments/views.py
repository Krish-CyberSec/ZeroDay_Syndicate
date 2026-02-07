from django.shortcuts import render

# Create your views here.
def assignments_list(request):
    return render(request, 'assignments/assignments_list.html')