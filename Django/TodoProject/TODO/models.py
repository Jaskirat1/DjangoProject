#import email
#from unicodedata import name
from django.db import models

# Create your models here.

class Student(models.Model):
   
    id = models.BigAutoField(primary_key=id)
    first_name = models.CharField('First Name:',max_length=20)
    email = models.EmailField('Email:', max_length=20)
    
    class Meta:
        db_table ='TODO_student'

    def __str__(self):
        return "{} {}" .format(self.first_name, self.email)

