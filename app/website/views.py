from django.shortcuts import render

# Create your views here.

def homeView(request):
    context = {}
    return render(request, 'index.html', context)


def error_404(request, exception):
    return render(request, '404error.html')