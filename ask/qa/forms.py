from django import forms
class AskForm(forms.form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea) 
	
	def clean_title(self):
		title = self.cleaned_data['title']
		return title + \
			"\n Thank you!"
	def clean_text(self):
		text = self.cleaned_data['text']
		return text + \
			"\n Thank you!"
	def save(self):
		ask = Question(**self.cleaned_data)
		ask.save()
		return ask
class AnswerForm(forms.form):
	text = forms.CharField(widget=forms.Textarea) 
	question = 
	def clean_title(self):
		title = self.cleaned_data['title']
		return title + \
			"\n Thank you!"
	def clean_text(self):
		text = self.cleaned_data['text']
		return text + \
			"\n Thank you!"
	def save(self):
		ask = Question(**self.cleaned_data)
		ask.save()
		return ask
		
