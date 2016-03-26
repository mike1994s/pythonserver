from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Star(models.Model):
	name = models.CharField(max_length=255)
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
#	author = models.ForeignKey(User, db_constraint=False)
#	author = models.IntegerField(default=1)
#	likes  = models.ManyToManyField(User, related_name='likes_set')
	def get_url(self):
		return "/star/" + str(self.pk) + "/"
	def __unicode__(self):
		return self.name
	class Meta:
		ordering = ['-added_at']

class News(models.Model):
	header = models.TextField()
	text = models.TextField()
	url = models.TextField()
	photo = models.TextField(default="")	
	added_at = models.DateField(auto_now_add=True)
	star =  models.ForeignKey(Star)
#	author = models.IntegerField(default=1)
	
	def get_url(self):
                return "/news/" + str(self.question_id) + "/"
	def __unicode__(self):
		return self.text
	class Meta:
		ordering = ['-added_at']
