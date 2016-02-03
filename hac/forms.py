from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email', 'phone_number']

	# Form validation
	# Django already has it's validators, by creating this validators
	# we're overridding those default validators
	# Python method for validating the form
	# Validation for full name
	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if full_name == '':
			raise forms.ValidationError("Name cannot be empty.")
		symbols = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
		for letter in full_name:
			if letter in symbols:
				raise forms.ValidationError("Name cannot contain symbols.")
		return full_name