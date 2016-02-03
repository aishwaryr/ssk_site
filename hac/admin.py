from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

# This class adds additional info on the admin page.
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	
	# Remove class Meta if customizing admin page in forms.py
	# do this 
	form = SignUpForm
	# class Meta:
	# 	model = SignUp
admin.site.register(SignUp, SignUpAdmin)