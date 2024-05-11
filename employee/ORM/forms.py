from django import forms
from .models import Reg_Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Reg_Employee
        fields = ['id','name', 'email', 'age', 'gender','phone_no','address','hno','street','city','state','work_experience','company_name',
                  'from_date','to_date','qualification','percentage','projects','title','description','photo']
        
        

    
