from django.db import models

# Create your models here.




# this is the create employee table
class Reg_Employee(models.Model):
    id=models.IntegerField(null=False,primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10)
    address = models.TextField(null=True)
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200,null=True)
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
    
   
    
    
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.id}'
    
    
    
    
    
    