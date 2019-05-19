from django.shortcuts import render
from account.forms import CreateProfileForm

def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
	else:
		if request.method == 'POST':
			# form = CreateProfieForm1(request.POST or None)
			form = CreateProfileForm(request.POST or None, request.FILES or None)
			
			
			if form.is_valid():
				username  = form.cleaned_data.get("username")
				email  = form.cleaned_data.get("email")
				password  = form.cleaned_data.get("password")
				first_name  = form.cleaned_data.get("category")
				new_user  = User.objects.create_user(username, email, password)
				return render(request, "account/registration_success.html")

		else:
			form = CreateProfileForm(request.POST or None) 
		context = {"form": form}
		return render(request, 'index.html', context)
def about(request):
	return render(request, 'about.html')
def contact(request):
	return render(request, 'contact.html')
