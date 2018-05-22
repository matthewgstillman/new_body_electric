from django.shortcuts import render, redirect

def index(request):
    src = "../static/new_body_electric-cropped_photo.png"
    context = {
        'src': src
    }
    return render(request, 'new_body_electric/index.html', context)