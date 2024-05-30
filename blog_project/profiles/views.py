from django.shortcuts import render,redirect
from . import forms

# Create your views here.


def profile(request):
    if request.method == 'POST':
        profile_form = forms.profile(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profiles')
    
    else:
     profile_form = forms.profile()   
    return render(request, 'profile.html', {'data' : profile_form})