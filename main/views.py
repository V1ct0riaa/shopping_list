from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Natanael Pascal Simbolon',
        'class': 'PBP Belajar Ulang'
    }

    return render(request, "main.html", context)