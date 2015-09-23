from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=30)
	begintime = models.DateField()
	endtime = models.DateField(blank=True)
	todo = models.TextField()
	def __unicode__(self):
		return self.name


class 	MyWish(models.Model):
	name =  models.CharField(max_length=30)
	why = models.TextField(blank=True)
	url = models.URLField(blank=True)
	price = models.FloatField(blank=True)
	begintime = models.DateField(blank=True)
	#project = models.ForeignKey(Project)
	project = models.ManyToManyField(Project,blank=True)
	def __unicode__(self):
		#return "%s %s %s" % (self.name,self.project,self.price)
		return self.name

