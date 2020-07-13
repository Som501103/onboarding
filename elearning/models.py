from django.db import models

class Check(models.Model):
    StaffID = models.CharField(max_length=10, unique=True, primary_key=True)
    Error_Detail = models.CharField(max_length=200, null=True)
    Date_check = models.DateTimeField(auto_now_add=True, null=True)

class Staff(models.Model):
    StaffID = models.CharField(max_length=10, unique=True, primary_key=True)
    StaffName = models.CharField(max_length=150)
    StaffPosition = models.CharField(max_length=10,null=True)
    StaffLevelcode = models.CharField(max_length=5,null=True)
    StaffDepshort = models.CharField(max_length=200)
    DeptCode = models.CharField(max_length=50)
    Organization = models.CharField(max_length=100)
    Date_Start = models.DateTimeField(auto_now_add=False, null=True)
    Date_PreTest = models.DateTimeField(auto_now_add=False, null=True)
    Score_PreTest = models.IntegerField(null=True, default=0)
    Vdo_pass = models.CharField(null=True,max_length=2,default='no')
    Date_Vdo = models.DateTimeField(auto_now_add=False, null= True)
    Date_PostTest = models.DateTimeField(auto_now_add=False, null= True)
    Score_PostTest = models.IntegerField(null=True, default=0)
