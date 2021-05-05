from django.shortcuts import render


def mentions(request):
    return render(request, 'mentions.html')
