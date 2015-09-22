from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=30)
	begintime = models.DateField(auto_now=True)
	endtime = models.DateField()
	todo = models.TextField()


class 	MyWish(models.Model):
	name =  models.CharField(max_length=30)
	url = models.URLField()
	price = models.FloatField()
	project = models.ForeignKey(Project)

