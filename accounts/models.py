
from django.db import models

# Create your models here.
class Constants:

    status = (
        ('yes', 'yes'),
        ('no', 'no')
    )
class Student(models.Model):
    Username = models.CharField(max_length=50, null=False, primary_key=True)
    emailid  = models.CharField(max_length=50, null=False, default="a@gmail.com")
    Course1 = models.CharField(max_length=150, null=False, choices=Constants.status)
    Course2 = models.CharField(max_length=150, null=False, choices=Constants.status)
    Course3 = models.CharField(max_length=150, null=False, choices=Constants.status)

