from django.shortcuts import render

def notes_list(request):
    return render(request, 'notes/notes_list.html')
