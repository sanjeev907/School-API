from django.db import models

# Create your models here.

class School(models.Model):
    Email = models.CharField(max_length=150)
    Name = models.CharField(max_length=150)
    City = models.CharField(max_length=150)
    Pincode = models.IntegerField()
    Password = models.CharField(max_length=100)
    Otp = models.IntegerField(default=0)
    

    def __str__(self):
        return self.Name


class Students(models.Model):
    School_name = models.ForeignKey(School, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150)
    Grade = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)

    def __str__(self):
        return self.Name