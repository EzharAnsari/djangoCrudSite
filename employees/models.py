from django.db import models



class UserAdd(models.Model):
    username = models.CharField(max_length=20,blank='false')
    name = models.CharField(max_length=50,blank='false')
    email = models.EmailField()
    mobileNo = models.IntegerField(default=0)
    password = models.CharField(max_length=256)


    def __str__(self):
        return self.name

        
class Student(models.Model):
    name = models.CharField(max_length=100,blank='false')
    branch = models.CharField(max_length=50,blank='false')
    year = models.IntegerField()
    rollNo = models.IntegerField()
    email = models.EmailField()
    mobileNo = models.IntegerField()
    image = models.ImageField(upload_to='Images/')

    def __str__(self):
        return self.name
