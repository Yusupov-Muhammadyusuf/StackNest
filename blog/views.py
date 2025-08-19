from django.shortcuts import render, redirect

def base_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
        
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def profile_view(request):
    return render(request, 'profile.html')

def public_view(request):
    return render(request, 'public.html')