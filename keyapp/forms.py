from django import forms
from keyapp.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'reg_no', 'dob']

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['dept', 'experience']

class salaryForm(forms.ModelForm):
    class Meta:
        model = salary
        fields = ['amount', 'shift']

    
