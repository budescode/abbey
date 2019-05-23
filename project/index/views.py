from django.shortcuts import render
from account.forms import CreateProfileForm

def home(request):
	return render(request, 'index1.html')
def about(request):
	return render(request, 'about.html')
def contact(request):
	return render(request, 'contact.html')
