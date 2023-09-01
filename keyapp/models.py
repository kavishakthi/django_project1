from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField(null=True)
    dob = models.DateField(null=True)

class Work(models.Model):
    reg_no = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='works')
    dept = models.CharField(max_length=100)
    experience = models.CharField(max_length=100, blank=True)

class salary(models.Model):
    reg_no = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='salary')
    amount = models.BigIntegerField(blank=True)
    shift = models.TextField(max_length=200)
    

 