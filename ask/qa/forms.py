from django import forms
from qa.models import Question, Answer
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea) 
	_user = User
	def clean_title(self):
		title = self.cleaned_data['title']
		return title
	def clean_text(self):
		text = self.cleaned_data['text']
		return text 

		
	def save(self):
		#question =Question(**self.cleaned_data)
		new_qs = Question(
				text=self.cleaned_data['text'], 
				title=self.cleaned_data['title'],
				author=_user
		)
		new_qs.save()			
		return new_qs
	def get_url(self):
		return "/question/" + str(self.pk) + "/"
class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea) 
	question = forms.IntegerField(widget=forms.HiddenInput()) 
	_user = User
	def save(self):
		
		answer = Answer(text = self.cleaned_data['text'],
				question=Question.objects.get(pk=self.cleaned_data['question']),
		author=_user)
		answer.save()
		return answer

class SignupForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def save(self):
		new_user=User.objects.create_user(self.cleaned_data['username'],
                                  self.cleaned_data['email'],
                                  self.cleaned_data['password'])
		new_user.save()
		new_user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		return new_user
	def login(self,user, request):
		login(request,user) 	
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	_user = User;
		
	def clean(self):
		_user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    		if _user is not None:
        		if _user.is_active:
 				return
        		else:
				raise forms.ValidationError(
					'You have banned',
					code='block'
				)
    		else:
			raise forms.ValidationError(
				'incorrect login or password',
				code='invalid'
			)
	def login(self, request):
            	login(request, _user)
		
