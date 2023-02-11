from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=50)
    address = models.CharField(max_length=30) 
    email = models.EmailField()

    
    def __str__(self):
        return self.domain
    
    class Meta:
        verbose_name_plural =  'company'
    

class Employee(models.Model):
    Emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30) 
    email = models.EmailField()
    position = models.CharField(max_length=20)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    contact_detail = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    contact_detail = models.CharField(max_length=10)


    def __str__(self):
        return self.name