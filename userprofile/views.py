from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileUpdateForm
from .models import Profile
from article.models import Article
from django.contrib.auth import get_user_model

def edit_profile(request):
    user = request.user
    
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    profile = user.profile

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'registration/edit_profile.html', {'form': form})