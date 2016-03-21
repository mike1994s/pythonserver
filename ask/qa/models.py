from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, db_constraint=False)
#	author = models.IntegerField(default=1)
	likes  = models.ManyToManyField(User, related_name='likes_set')
	def get_url(self):
		return "/question/" + str(self.pk) + "/"
	def __unicode__(self):
		return self.title
	class Meta:
		ordering = ['-added_at']

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question =  models.ForeignKey(Question)
#	author = models.IntegerField(default=1)
	author = models.ForeignKey(User, db_constraint=False)
	
	def get_url(self):
                return "/question/" + str(self.question_id) + "/"
	def __unicode__(self):
		return self.text
	class Meta:
		ordering = ['-added_at']
