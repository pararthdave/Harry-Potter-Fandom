from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    subject=models.CharField( max_length=122)
    message=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.email

class Pb1(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb2(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb3(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb4(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb5(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb6(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name

class Pb7(models.Model):
    name= models.CharField( max_length=50)
    email=models.CharField( max_length=122)
    remarks=models.TextField("")
    date=models.DateField()
    def __str__(self):
        return self.name


    


