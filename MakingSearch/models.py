from django.db import models

# Create your models here.
class Search(models.Model):
	user_search=models.CharField(max_length=50)
	date=models.DateField(auto_now=True)
	#data=data.auto_now_add()

	def __str__(self):
		return self.user_search,self.date