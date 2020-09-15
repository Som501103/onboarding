from django.db import models

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    CourseBy = models.CharField(max_length=50)
    Couse_Sub_Total = models.IntegerField(null=True, default=0)
    Course_Total_QS = models.IntegerField(null=True, default=0)
    Course_Pass_Score = models.IntegerField(null=True, default=0)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    Cover_img = models.CharField(max_length=50,null=True)
    CourseStatus = models.CharField(null=True,max_length=3,default='OFF')

class Sub_Course(models.Model):
    Title = models.CharField(max_length=100)
    ConstructorName = models.CharField(max_length=100, null=True)
    ConstructorPosition = models.CharField(max_length=100, null=True)
    Tel = models.CharField(max_length=7,null=True,default='0000')
    email = models.EmailField(null=True, default='uuu@pea.co.th')
    Document = models.URLField(max_length=300, null=True)
    URLGdrive = models.URLField(max_length=300, null=True)
    TotalTime =models.IntegerField(null=True, default=0)
    Date_Created = models.DateField(auto_now_add=True, null=True)
    Link_Course = models.ForeignKey(Course,related_name='Sub_Courses',on_delete = models.CASCADE,null= True)

class Course_Pretest(models.Model):
    TestTitle = models.CharField(max_length=300)
    Test1 = models.CharField(max_length=200, null=True)
    Test2 = models.CharField(max_length=200, null=True)
    Test3 = models.CharField(max_length=200, null=True)
    Test4 = models.CharField(max_length=200, null=True)
    Test_ans = models.CharField(max_length=200, null=True)
    Test_Course = models.ForeignKey(Course,related_name='Courses',on_delete = models.CASCADE,null= True)

class Check(models.Model):
    StaffID = models.CharField(max_length=10, unique=True, primary_key=True)
    Error_Detail = models.TextField(default='error',blank=True, null=True)
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
    Status = models.CharField(max_length=12, default='on Process', null=True)

class Staff_Score(models.Model):
    Pre_Created = models.DateTimeField(auto_now_add=False, null= True)
    Pre_Score = models.IntegerField(null=True, default=0)
    Post_Created = models.DateTimeField(auto_now_add=False, null= True)
    Post_Score = models.IntegerField(null=True, default=0)
    Staff = models.ForeignKey(Staff, related_name= 'Staff_score', on_delete= models.CASCADE,null= True)
    Link_course = models.ForeignKey(Course, related_name='Course_Score', on_delete=models.CASCADE,null= True)

class Staff_Vdolog(models.Model):
    Date_Created = models.DateTimeField(auto_now_add=False, null= True)
    Status = models.CharField(max_length=12, default='on Process', null=True)
    Link_SubCourse = models.ForeignKey(Sub_Course, related_name='SubCourse_Vdo', on_delete=models.CASCADE,null= True)
    Link_course = models.ForeignKey(Course, related_name='Course_Vdo', on_delete=models.CASCADE,null= True)
    Staff = models.ForeignKey(Staff, related_name= 'Staff_Vdo', on_delete= models.CASCADE,null= True)

class Feedback(models.Model):
    Title = models.CharField(max_length=300)
    Detail = models.TextField(default='detail',blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=False, null= True)
    Staff = models.ForeignKey(Staff, related_name= 'Staff_feedback', on_delete= models.CASCADE,null= True)

class Evaluate_t(models.Model):
    No_1 = models.IntegerField(default=0)
    No_2 = models.IntegerField(default=0)
    No_3 = models.IntegerField(default=0)
    No_4 = models.IntegerField(default=0)
    No_5 = models.IntegerField(default=0)
    No_6 = models.IntegerField(default=0)
    No_7 = models.IntegerField(default=0)
    No_8 = models.IntegerField(default=0)
    No_9 = models.IntegerField(default=0)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)
    Status = models.BooleanField(default=False)
    Link_course = models.ForeignKey(Course, related_name='Course_Eva', on_delete=models.CASCADE,null= True)
    Staff = models.ForeignKey(Staff, related_name= 'Staff_Eva', on_delete= models.CASCADE,null= True)

class Closed_class(models.Model):
    id = models.AutoField(primary_key=True)
    StaffID = models.CharField(max_length=10)
    Link_course = models.ForeignKey(Course, related_name='Course_Closed', on_delete=models.CASCADE,null= True)
    Status = models.BooleanField(default=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)

class Hub_test(models.Model):
    id = models.AutoField(primary_key=True)
    StaffID = models.CharField(max_length=10)
    no1 = models.TextField(default='ข้อ1',blank=True, null=True)
    no1_Score = models.IntegerField(default=0,null=True)
    no2_1 = models.TextField(default='ข้อ2_1',blank=True, null=True)
    no2_1_Score = models.IntegerField(default=0,null=True)
    no2_2 = models.TextField(default='ข้อ2_2',blank=True, null=True)
    no2_2_Score = models.IntegerField(default=0,null=True)
    no2_3 = models.TextField(default='ข้อ2_3',blank=True, null=True)
    no2_3_Score = models.IntegerField(default=0,null=True)
    no2_4 = models.TextField(default='ข้อ2_4',blank=True, null=True)
    no2_4_Score = models.IntegerField(default=0,null=True)
    no2_5 = models.TextField(default='ข้อ2_5',blank=True, null=True)
    no2_5_Score = models.IntegerField(default=0,null=True)
    no3 = models.TextField(default='ข้อ3',blank=True, null=True)
    no3_Score = models.IntegerField(default=0,null=True)
    no4 = models.TextField(default='ข้อ4',blank=True, null=True)
    no4_Score = models.IntegerField(default=0,null=True)
    no5 = models.TextField(default='ข้อ5',blank=True, null=True)
    no5_Score = models.IntegerField(default=0,null=True)
    no6 = models.TextField(default='ข้อ6',blank=True, null=True)
    no6_Score = models.IntegerField(default=0,null=True)
    no7 = models.TextField(default='ข้อ7',blank=True, null=True)
    no7_Score = models.IntegerField(default=0,null=True)
    no8 = models.TextField(default='ข้อ8',blank=True, null=True)
    no8_Score = models.IntegerField(default=0,null=True)
    no9 = models.TextField(default='ข้อ9',blank=True, null=True)
    no9_Score = models.IntegerField(default=0,null=True)
    no10 = models.TextField(default='ข้อ10',blank=True, null=True)
    no10_Score = models.IntegerField(default=0,null=True)
    Status = models.CharField(default=0, null=True, max_length =1)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)
    # Status 0 notest  1 waiting 2 pass 3 false

class Bu_test(models.Model):
    id = models.AutoField(primary_key=True)
    StaffID = models.CharField(max_length=10)
    no1 = models.TextField(default='ข้อ1',blank=True, null=True)
    Status = models.CharField(default=0, null=True, max_length =1)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)