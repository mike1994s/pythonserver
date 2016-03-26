from django import forms
from news.models import Star
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
class StarForm(forms.Form):
	name = forms.CharField(max_length=255)
	def clean_title(self):
		name = self.cleaned_data['name']
		return name
	def save(self):
		#question =Question(**self.cleaned_data)
		star = Star(
				name=self.cleaned_data['name']
		)
		star.save()			
		return star
	def get_url(self):
		return "/star/" + str(self.pk) + "/"
