from django.shortcuts import render
from .forms import SignUpForm

def home(request):
	title = "My title %s" %(request.user)
	# SignUpForm from forms.py
	form = SignUpForm()
	# Here we're setting the context if we use the template_title from the 
	# below dictionary in home.html it will show the title set above
	context = {
				"template_title": title,
				"form": form
	}
	return render(request, "home.html", context)