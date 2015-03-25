from django.db import models

# Create your models here.
class Person(models.Model):
	IDperson = models.AutoField(primary_key=True)
	personName = models.TextField()
	personNumber = models.IntegerField()

	def __unicode__(self):
		return "%d : %s , %d"%(self.IDperson, self.personName,self.personNumber,)

class Candidates(models.Model):
	IDcandidates = models.AutoField(primary_key=True)
	personID = models.IntegerField()
	cnt = models.IntegerField(default=0)

	def __unicode__(self):
		return "%d : %d"%(self.IDcandidates, self.personID,)