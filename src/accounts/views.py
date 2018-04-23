from django.shortcuts import render, redirect
from accounts.forms import( 
    RegistrationForm, 
	EditProfile, 
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse



#from django.contrib.auth.forms import UserCreationForm   (for default registration form)
@login_required
def home(request):
	return render(request, 'accounts/home.html',{})

# for custom registration form
def register(request):
	if request.method == 'POST':

		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:home'))
		else:
			args={'form':form}
			return render(request,'accounts/register.html', args)	
	else:
		form = RegistrationForm()
		args={'form':form}
		return render(request,'accounts/register.html', args)		
	

# -----------------------------------------------------------------------------
# (for default register form)
# def register(request):
# 	if request.method == 'POST':
# 		form = UserCreationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/account')
# 	else:
# 		form = UserCreationForm()
# 		args={'form':form}
# 		return render(request,'accounts/register.html', args)
# ----------------------------------------------------------------------------
@login_required
def view_profile(request):
	args = {'user': request.user}
	return render(request,'accounts/profile.html', args)	

# for (coustomised edit profile)
@login_required
def edit_profile(request):
	if request.method=='POST':
		form = EditProfile(request.POST,instance=request.user)

		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:view_profile'))
	else:
		form = EditProfile(instance=request.user)
		args = {'form':form}
		return render(request,'accounts/edit_profile.html',args)

# -----------------------------------------------------------------------------------

# for (default edit profile)
# def edit_profile(request):
# 	if request.method=='POST':
# 		form = UserChangeForm(request.POST,instance=request.user)

# 		if form.is_valid():
# 			form.save()
# 			return redirect('/account/profile')
# 	else:
# 		form = UserChangeForm(instance=request.user)
# 		args = {'form':form}
# 		return render(request,'accounts/edit_profile.html',args)

#-----------------------------------------------------------------------------------------
# change password for the logged in  user
@login_required
def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST,user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect(reverse('accounts:view_profile'))
		else:
			print(form.errors)
			
			return redirect(reverse('accounts:change_password'))

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request,'accounts/change_password.html',args)
	

   










   
 
	    

	