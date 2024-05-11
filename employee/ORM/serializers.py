from rest_framework import serializers
from .models import Reg_Employee,Photo

class EmployeeSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Reg_Employee
        fields = '__all__'
    
    
    
    
    
    
    
    
class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Employee
        fields = ['name', 'email', 'age', 'gender']  # Specify only the required fields for update
        
        
        
        

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'uploaded_at')