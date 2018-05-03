from django.shortcuts import render


def index(request):
    return render(request, 'dna/index.html', {})
