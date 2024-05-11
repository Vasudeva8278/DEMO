from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'age', 'gender','phone_no','address_details','hno','street','city','state','work_experience','company_name',
                  'from_date','to_date','qualification','percentage','projects','title','description','photo']
        
        

    
