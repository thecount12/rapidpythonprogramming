#views.py
from django.contrib.auth import login, authenticate 
from django.shortcuts import render, redirect 
from signup.forms import SignUpForm
def Signup(request): 
	if request.method == 'POST': 
		form = SignUpForm(request.POST) 
		if form.is_valid(): 
			user = form.save() 
			user.refresh_from_db() # load the profile
			user.profile.birthdate = form.cleaned_data.get('birth_date') 
			user.save() 
			raw_password = form.cleaned_data.get('password1') 
			user = authenticate(username=user.username, password=raw_password) 
			login(request, user) return redirect('/') 
	else: 
		form = SignUpForm() 
	return render(request, 'signup.html', {'form': form}) 
