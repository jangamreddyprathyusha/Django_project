#user defined field

from django import forms 
from hr_department.models import emp_table 

class employee_form(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=emp_table