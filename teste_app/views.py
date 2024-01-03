from django.shortcuts import render

def sua_view(request):
    return render(request, 'index.html')