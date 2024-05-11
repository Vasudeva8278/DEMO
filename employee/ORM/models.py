from django.db import models

# Create your models here.




# this is the create employee table
class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    address_details = models.TextField()
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    work_experience = models.IntegerField() 
    company_name = models.CharField(max_length=200)  
    from_date = models.DateField()  # Changed field name to lowercase for consistency
    to_date = models.DateField()  # Changed field name to lowercase for consistency
    qualification = models.CharField(max_length=100)
    percentage = models.CharField(max_length=5)
    projects = models.TextField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    