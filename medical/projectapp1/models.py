

# Create your models here.
from django.db import models

# Create your models here.
class Medicalstore(models.Model):
    Medicine=models.CharField(max_length=25,null=True)
    Brand=models.CharField(max_length=60,null=True)
    Price=models.CharField(max_length=12,null=True)

    def __str__(self) :
        return self.Medicine