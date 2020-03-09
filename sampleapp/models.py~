from django.db import models

# Create your models here.



class Couple(models.Model):
	hus_name = models.CharField(max_length=20)
	wife_name = models.CharField(max_length=20)
	phone = models.CharField(max_length=15, default="")
	email = models.EmailField()
	comment = models.TextField()
	#union_id = models.CharField(default="")
	pub_date = models.DateTimeField("date published")

	def __str__(self):
		return self.email

