from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'about', 'location', 'email', 'link_1', 'link_2', 'link_3']