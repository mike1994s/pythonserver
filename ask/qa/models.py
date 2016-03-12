from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.OneToOneField(User)
	likes  = models.ForeignKey(User,related_name='likes', null=True, on_delete=models.CASCADE)
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.OneToOneField(Question,related_name='question')
	author = models.OneToOneField(User)
	def __unicode__(self):
		return self.text
	class Meta:
		ordering = ['-added_at']
