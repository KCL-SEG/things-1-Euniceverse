from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

# Create your models here.
class Things(models.Model):
	name = models.CharField(
		unique=True,
		blank=False,
		max_length=30
	)
	
	description = models.CharField(
		blank=True,
		max_length=120
	)
	
	quantity =  models.IntegerField(
		validators=[
			MinValueValidator(0, "The number can not be smaller than 0"),
			MaxValueValidator(100, "The number can not be bigger than 100")
		] 	
	)

