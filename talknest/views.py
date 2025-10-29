from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home_user.html')
    else:
        return render(request, 'home_guest.html')
