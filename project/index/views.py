from django.shortcuts import render
from account.forms import CreateProfileForm

def home(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'index1.html')
def contact(request):
	return render(request, 'contact.html')
