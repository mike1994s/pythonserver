from django import forms
from qa.models import Question, Answer
class AskForm(forms.Form):
	title = forms.CharField(max_length=255)
	text = forms.CharField(widget=forms.Textarea) 
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
				title=self.cleaned_data['title']
		)
		new_qs.save()			
		return new_qs
	def get_url(self):
		return "/question/" + str(self.pk) + "/"
class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea) 
	question = forms.IntegerField(widget=forms.HiddenInput()) 
	def save(self):
		
		answer = Answer(text = self.cleaned_data['text'],
				question=Question.objects.get(pk=self.cleaned_data['question']))
		answer.save()
		return answer
		
