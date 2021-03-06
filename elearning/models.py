from django.db import models

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    Course_Type  = models.CharField(max_length = 2, default='1')
    CourseBy = models.CharField(max_length=50)
    Couse_Sub_Total = models.IntegerField(null=True, default=0)
    Course_Total_QS = models.IntegerField(null=True, default=0)
    Course_Pass_Score = models.IntegerField(null=True, default=0)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    Cover_img = models.CharField(max_length=50,null=True)
    CourseStatus = models.CharField(null=True,max_length=3,default='OFF') #ON =เปิดให้เข้าเรียน OFF = ปิดการมองเห็น COM = เปิดการมองเห็นแต่ยังไม่เปิดให้เรียน
    Start_date = models.DateField(default='2021-06-01')
    End_date = models.DateField(default='2021-11-30')
    Total_people = models.IntegerField(default=838)
    Pre_Test = models.BooleanField(default=True)
    Post_Test = models.BooleanField(default=True)
    # course_type 1 = ภาคบังคับ 2 = ภาคเสรี

class Sub_Course(models.Model):
    Title = models.CharField(max_length=100)
    ConstructorName = models.CharField(max_length=100, null=True)
    ConstructorPosition = models.CharField(max_length=100, null=True)
    Tel = models.CharField(max_length=7,null=True,default='0000')
    email = models.EmailField(null=True, default='uuu@pea.co.th')
    Document = models.URLField(max_length=300, null=False,blank=True)
    URLGdrive = models.URLField(max_length=300, null=True,blank=True)
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
    StaffPosition = models.CharField(max_length=20,null=True,default='ตำแหน่ง')
    StaffLevelcode = models.CharField(max_length=5,null=True)
    StaffDepshort = models.CharField(max_length=200)
    DeptCode = models.CharField(max_length=50)
    Short_Part_Dept = models.CharField(max_length=10,default='สายงาน',null=True)
    Organization = models.CharField(max_length=100)
    Date_Start = models.DateTimeField(auto_now_add=False, null=True)
    Status = models.CharField(max_length=12, default='on Process', null=True)

class Staff_Score(models.Model):
    Pre_Created = models.DateTimeField(auto_now_add=False, null= True)
    Pre_Score = models.IntegerField(null=True, default=0)
    Post_Created = models.DateTimeField(auto_now_add=False, null= True)
    Post_Score = models.IntegerField(null=True, default=0)
    Check_policy =  models.IntegerField(default=0,null=True) #0=ไม่ได้ยอมรับข้อกำหนด 1= ยอมรับ
    Status = models.IntegerField(default=0,null=True) #0 = ยังเรียนไม่จบ 1 = จบแล้ว
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

class Topic_Evaluate(models.Model):
    Topic = models.CharField(max_length=300)
    Order = models.CharField(max_length=2)
    Sub_Course = models.ForeignKey(Sub_Course,related_name='Sub_Courses',on_delete = models.CASCADE,null= True)

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
    Usability = models.CharField(default='การนำไปใช้',max_length=300,blank=True, null=True)
    Future_Subject = models.CharField(default='หัวข้อที่สนใจ',max_length=300,blank=True, null=True)
    Suggestion = models.TextField(default='ข้อเสนอแนะ',blank=True, null=True)
    KM_Gender = models.CharField(default='-',max_length=1,blank=True, null=True)
    KM_Generation = models.CharField(default='Gen',max_length=20,blank=True, null=True)
    KM_B1 = models.IntegerField(default=0)
    KM_Day = models.IntegerField(default=0,null=True)
    KM_Training = models.IntegerField(default=0,null=True)
    KM_Meeting = models.IntegerField(default=0,null=True)
    KM_DDoc = models.IntegerField(default=0,null=True)
    KM_Leaflets = models.IntegerField(default=0,null=True)
    KM_email = models.IntegerField(default=0,null=True)
    KM_Vdo = models.IntegerField(default=0,null=True)
    KM_Social = models.IntegerField(default=0,null=True)
    KM_B3 = models.IntegerField(default=0)
    KM_B4 = models.IntegerField(default=0)
    KM_B5 = models.TextField(default='ข้อเสนอแนะ',blank=True, null=True)
    courseid21_no1_score = models.IntegerField(default=0)
    courseid21_no2_score = models.IntegerField(default=0)
    courseid21_no3_score = models.IntegerField(default=0)
    courseid21_no4_score = models.IntegerField(default=0)
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
    StaffID = models.ForeignKey(Staff, related_name= 'Staff_testihub', on_delete= models.CASCADE,null= True)
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
    total = models.IntegerField(default=0,null=True)
    feedback = models.TextField(blank=True, null=True)
    Status = models.CharField(default=0, null=True, max_length =1)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)
    # Status 0 notest  1 waiting 2 pass 3 false 4 testagain

class Bu_test(models.Model):
    id = models.AutoField(primary_key=True)
    StaffID = models.CharField(max_length=10)
    no1 = models.TextField(default='ข้อ1',blank=True, null=True)
    Status = models.CharField(default=0, null=True, max_length =1)
    Date_Created = models.DateTimeField(auto_now_add=True, null= True)

class virtual_class(models.Model):
    PK_id = models.AutoField(primary_key=True)
    Activity_name = models.CharField(max_length=250,null=True)
    Activity_generation = models.IntegerField(default=1)
    Date_zoom = models.DateField()
    Time_zoom = models.TimeField()
    Endtime_zoom = models.TimeField(default='00:00')
    lecturer_name = models.CharField(max_length=500 , null=True)
    Num_people = models.IntegerField(default=0)
    Link_zoom = models.CharField(max_length=250,null=True)
    meeting_id = models.CharField(max_length=250,null=True)
    Status = models.BooleanField(default=True)#True เปิด False ปิด

class Dept(models.Model):
    PK_ID = models.AutoField(primary_key=True)
    listname = models.CharField(max_length=10,null=True)
    max_number = models.IntegerField(default=0,null=True)
    current_number = models.IntegerField(default=0 , null=True)
    percent_number = models.FloatField(default=0.00 , null=True,blank=True)

class county(models.Model):
    PK_ID = models.AutoField(primary_key=True)
    county_name = models.CharField(max_length=10,null=True)
    max_number = models.IntegerField(default=0,null=True)
    current_number = models.IntegerField(default=0 , null=True)
    percent_number = models.FloatField(default=0.00 , null=True,blank=True)