from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    usertype = models.CharField(max_length=100, null=True, blank=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=25, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Gender = models.CharField(max_length=6, null=True, blank=True)
    Email = models.CharField(max_length=20, null=True, blank=True)
    Phone_no = models.BigIntegerField(null=True, blank=True)
    Place = models.CharField(max_length=25, null=True, blank=True)

class ComplaintsTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Complaints = models.CharField(max_length=500, null=True, blank=True)
    Reply = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField(auto_now_add=True)

class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Rating = models.IntegerField(null=True, blank=True)
    Feedback = models.CharField(max_length=300)
    Date = models.DateField(auto_now_add=True)

class SignTable(models.Model):
    SignName = models.CharField(max_length=5, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)