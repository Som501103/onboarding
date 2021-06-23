from django.contrib.auth import models
from .models import Staff, Check, Course, Sub_Course, Course_Pretest, Staff_Score, Staff_Vdolog, Feedback, Evaluate_t, Closed_class, Hub_test
from rest_framework import serializers


class request_Sub_Course(serializers.ModelSerializer):
	class Meta:
		model = Sub_Course
		fields = ['Title','ConstructorName', 'ConstructorPosition','Tel','email','Document','URLGdrive']

class request_Course(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['CourseName','CourseBy', 'CourseStatus','Couse_Sub_Total','Course_Total_QS','Course_Pass_Score','Start_date','End_date','Total_people','Date_Created','Cover_img','CourseStatus','Pre_Test','Post_Test']
