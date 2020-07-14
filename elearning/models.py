from django.db import models

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    CourseBy = models.CharField(max_length=50)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    CourseStatus = models.CharField(null=True,max_length=2,default='OFF')

class Sub_Course(models.Model):
    Title = models.CharField(max_length=100)
    ConstructorName = models.CharField(max_length=100)
    ConstructorPosition = models.CharField(max_length=100)
    Document = models.URLField(max_length=300)
    Date_Created = models.DateField(auto_now_add=True, null=True)
    Link_Course = models.ForeignKey(Course,related_name='Sub_Courses',on_delete = models.CASCADE,null= True)

class Course_Pretest(models.Model):
    TestTitle = models.CharField(max_length=300)
    Test1 = models.CharField(max_length=200)
    Test2 = models.CharField(max_length=200)
    Test3 = models.CharField(max_length=200)
    Test4 = models.CharField(max_length=200)
    Test_Course = models.ForeignKey(Course,related_name='Courses',on_delete = models.CASCADE,null= True)

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
    Date_PreTest1 = models.DateTimeField(auto_now_add=False, null=True)
    Score_PreTest1 = models.IntegerField(null=True, default=0)
    Vdo_pass1_1 = models.CharField(null=True,max_length=2,default='no')
    Date_Vdo1_1 = models.DateTimeField(auto_now_add=False, null= True)
    Vdo_pass1_2 = models.CharField(null=True,max_length=2,default='no')
    Date_Vdo1_2 = models.DateTimeField(auto_now_add=False, null= True)
    Vdo_pass1_3 = models.CharField(null=True,max_length=2,default='no')
    Date_Vdo1_3 = models.DateTimeField(auto_now_add=False, null= True)
    Date_PostTest1 = models.DateTimeField(auto_now_add=False, null= True)
    Score_PostTest1 = models.IntegerField(null=True, default=0)
