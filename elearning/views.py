from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
import requests, xmltodict
from .models import Staff, Check, Course, Sub_Course, Course_Pretest, Staff_Score, Staff_Vdolog
import string
from datetime import datetime
from itertools import zip_longest
import re

# Create your views here.

def login(request):
    mgs = {
                    'massage' : ' '
                }
    if request.method == 'POST':
        Emp_id = request.POST.get('userID')
        Emp_pass = str(request.POST.get('passwordID'))

        # print(Emp_id,Emp_pass)
        check = Check.objects.filter(StaffID=Emp_id).count()
        if check == 1:
            reposeMge = 'true'
        # if Emp_id == '300109' or Emp_id == '498433' or Emp_id == '505397' or Emp_id == '495186' or  Emp_id =='510117' or Emp_id == '504636' or Emp_id == '499700' or Emp_id == '499691' or Emp_id == '499734' or Emp_id == '498610' :
        #     reposeMge = 'true'
            #มีปัญหากับการเช็คpassword ผ่านidm
        else:
            check_ID = idm_login(Emp_id,Emp_pass)
            # print(check_ID)
            reposeMge = check_ID
        
        if reposeMge == 'true':
                nameget = idm(Emp_id)
                # print(nameget)
                Fullname = nameget['TitleFullName']+nameget['FirstName']+' '+nameget['LastName']
                Position = nameget['PositionDescShort']
                LevelCode = nameget['LevelCode']
                Dept = nameget['DepartmentShort']
                Dept_code = nameget['NewOrganizationalCode']
                RegionCode = nameget['RegionCode']
                request.session['Emp_id'] = Emp_id
                request.session['Fullname'] = Fullname
                request.session['Position'] = Position
                request.session['LevelCode'] = LevelCode
                request.session['Department'] = Dept
                request.session['Dept_code'] = Dept_code
                request.session['RegionCode'] = RegionCode 
                # 9900
                check_user = Staff.objects.filter(StaffID=Emp_id).count()
                if check_user == 0 :
                    Staff_save = Staff(
                        StaffID = Emp_id,
                        StaffName = Fullname,
                        StaffPosition = Position,
                        StaffLevelcode = LevelCode,
                        StaffDepshort = Dept,
                        DeptCode = Dept_code,
                        Organization = RegionCode,
                    )
                    Staff_save.save()

                    return redirect('home')
                else:
                    Staff_score = Staff.objects.get(StaffID = Emp_id)
                    print(Staff_score)
                return redirect('home')
        else:
                mgs = {
                    'massage' : 'รหัสพนักงานหรือรหัสผ่านไม่ถูกต้อง....'
                }
                # return redirect('login',{'mgs':mgs})

    return render(request,'login.html',{'mgs':mgs})

def menu(request):
    Profile ={
        'Emp_id' : request.session['Emp_id'],
        'Fullname' : request.session['Fullname'],
        'Position' : request.session['Position'],
        'LevelCode' : request.session['LevelCode'],
        'Dept' : request.session['Department'],
        'RegionCode' : request.session['RegionCode']
    }
    
    return render(request,'menu.html',{'Profile':Profile})

def home(request):
    Emp_id = request.session['Emp_id']
    Fullname = request.session['Fullname']
    Position = request.session['Position']
    LevelCode = request.session['LevelCode']
    Dept = request.session['Department']
    RegionCode = request.session['RegionCode']
    # Score = Staff_Score.objects.get(StaffID = Emp_id)
    Course_all = Course.objects.all()
    Course_score = Staff_Score.objects.select_related('Link_course').filter(Staff = Staff.objects.get(StaffID = Emp_id))
    combined_results = list(zip_longest(Course_all, Course_score))
    print(combined_results)
    
    Profile= {
        'Emp_id' : Emp_id,
        'Fullname' : Fullname,
        'Position' : Position,
        'LevelCode' : LevelCode,
        'Dept' : Dept,
        'RegionCode':RegionCode,
        }
    return render(request, 'home.html',{'Profile':Profile, 'Course_all': Course_all ,'combined_results':combined_results,'Course_score':Course_score})

def idm_login(Emp_id, Emp_pass):
    # Emp_passc = str(Emp_pass)
    print('--------------------')
    
    url="https://idm.pea.co.th/webservices/idmservices.asmx?WSDL"
    headers = {'content-type': 'text/xml'}
    xmltext ='''<?xml version="1.0" encoding="utf-8"?>
                 <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                    <soap:Body>
                        <IsValidUsernameAndPassword_SI xmlns="http://idm.pea.co.th/">
                        <WSAuthenKey>{0}</WSAuthenKey>
                        <Username>{1}</Username>
                        <Password>{2}</Password>
                        </IsValidUsernameAndPassword_SI>
                    </soap:Body>
                </soap:Envelope>'''
    wskey = '07d75910-3365-42c9-9365-9433b51177c6'
    body = xmltext.format(wskey,Emp_id,Emp_pass)
    response = requests.post(url,data=body,headers=headers)
    print(response.status_code)
    o = xmltodict.parse(response.text)
    jsonconvert=dict(o)
    # print(o)
    authen_response = jsonconvert["soap:Envelope"]["soap:Body"]["IsValidUsernameAndPassword_SIResponse"]["IsValidUsernameAndPassword_SIResult"]["ResultObject"]
    return authen_response

def idm(Emp_id):
    url="https://idm.pea.co.th/webservices/EmployeeServices.asmx?WSDL"
    headers = {'content-type': 'text/xml'}
    xmltext ='''<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <GetEmployeeInfoByEmployeeId_SI xmlns="http://idm.pea.co.th/">
                        <WSAuthenKey>{0}</WSAuthenKey>
                        <EmployeeId>{1}</EmployeeId>
                        </GetEmployeeInfoByEmployeeId_SI>
                </soap:Body>
                </soap:Envelope>'''
    wsauth = 'e7040c1f-cace-430b-9bc0-f477c44016c3'
    body = xmltext.format(wsauth,Emp_id)
    response = requests.post(url,data=body,headers=headers)
    o = xmltodict.parse(response.text)

    # print(o)
    jsonconvert=o["soap:Envelope"]['soap:Body']['GetEmployeeInfoByEmployeeId_SIResponse']['GetEmployeeInfoByEmployeeId_SIResult']['ResultObject']
    employeedata = dict(jsonconvert)
    print(employeedata['FirstName'])
    return employeedata

def Course_main(request, PK_Course_D):
    Emp_id = request.session['Emp_id']

    Profile ={
        'Fullname' : request.session['Fullname'],
        'Position' : request.session['Position'],
        'LevelCode' : request.session['LevelCode'],
        'Dept' : request.session['Department'],
        'RegionCode' : request.session['RegionCode']
    }
    

    Course_detail = Course.objects.get(id=PK_Course_D)
    Staff_score_check = Staff_Score.objects.filter(Staff = Staff.objects.get(StaffID = Emp_id), Link_course = Course.objects.get(id = PK_Course_D)).count
    if Staff_score_check == 0:
        Staff_prescore_create = Staff_Score(
                    Pre_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    Pre_Score = 0,
                    Post_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    Post_Score = 0,
                    Staff = Staff.objects.get(StaffID = Emp_id),
                    Link_course = Course.objects.get(id = PK_Course_D)
                    )
        Staff_prescore_create.save()
    else:
        Staff_score = Staff_Score.objects.get(Staff = Staff.objects.get(StaffID = Emp_id), Link_course = Course.objects.get(id = PK_Course_D))
        pre = Staff_score.Pre_Score
        post = Staff_score.Post_Score

    Sub_course = Sub_Course.objects.filter(Link_Course = Course.objects.get(id=PK_Course_D))
    # Sub_course_check = Sub_Course.objects.all().prefetch_related('SubCourse_Vdo').filter(Link_Course = Course.objects.get(id=PK_Course_D)).values()

    Sub_course_check = Staff_Vdolog.objects.all().filter(Link_course = Course.objects.get(id=PK_Course_D))
    combined_results = list(zip_longest(Sub_course, Sub_course_check))
    # print(combined_results[0][0].Title)
    # for x in combined_results:
    #     print(x[0].id)

    # print(Sub_course.query)
    # print(Sub_course_check.query)
    # print(Sub_course_check)
    # Staff_score = Staff_Score.objects.get(Staff = Staff.objects.get(StaffID = Emp_id))
    vdo = Staff_Vdolog.objects.filter(Status = 'Done',Staff = Staff.objects.get(StaffID = Emp_id),Link_course = Course.objects.get(id=PK_Course_D)).count()
    B_colour = check(Course_detail.Couse_Sub_Total,vdo)
    # print(vdo)
    # print(Course_detail.CourseName)
    # print(Staff_score.Pre_Score1)
    
    return render(request, 'Course_main.html',{'Profile':Profile,'Course_detail': Course_detail, 'Sub_course': Sub_course,'Sub_course_check':Sub_course_check, 'pre':pre, 'post':post, 'vdo': vdo, 'B_colour': B_colour, 'combined_results':combined_results})

def VDO(request, PK_Title):
    Emp_id = request.session['Emp_id']
    Profile ={
        'Fullname' : request.session['Fullname'],
        'Position' : request.session['Position'],
        'LevelCode' : request.session['LevelCode'],
        'Dept' : request.session['Department'],
        'RegionCode' : request.session['RegionCode']
    }
    Sub_course = Sub_Course.objects.select_related('Link_Course').get(id = PK_Title )
    print(Sub_course.Link_Course.id)
    if request.method == 'POST':
        check = Staff_Vdolog.objects.filter(Staff=Emp_id, Link_SubCourse = PK_Title).count()
        if check == 0:
            Staff_vdo_save = Staff_Vdolog(
                            Date_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            Status = 'Done',
                            Link_SubCourse = Sub_Course.objects.get(id = PK_Title),
                            Link_course = Course.objects.get(id = Sub_course.Link_Course.id),
                            Staff = Staff.objects.get(StaffID = Emp_id)
                        )
            Staff_vdo_save.save()
        else:
            Staff_vdo_update = Staff_Vdolog.objects.get(Staff=Emp_id, Link_SubCourse = PK_Title)
            Staff_vdo_update.Date_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Staff_vdo_update.Status = 'Done'
            Staff_vdo_update.save()
        
        return redirect('Course_main',PK_Course_D=Sub_course.Link_Course.id)
    
    return render(request, 'VDO.html',{'Profile':Profile,'Sub_course': Sub_course})

def check(Couse_Sub_Total,vdo):
    if Couse_Sub_Total == vdo:
        colour = 'Done'
    else:
        colour = 'False'
    return colour

def pretest(request, PK_Course_D):
    Emp_id = request.session['Emp_id']
    Profile ={
        'Fullname' : request.session['Fullname'],
        'Position' : request.session['Position'],
        'LevelCode' : request.session['LevelCode'],
        'Dept' : request.session['Department'],
        'RegionCode' : request.session['RegionCode']
    }
    Course_item = Course.objects.get(id = PK_Course_D)
    Question = Course_Pretest.objects.select_related('Test_Course').filter(Test_Course = Course.objects.get(id = PK_Course_D)).order_by('?')
    # print(Question)
    if request.method == 'POST':
        sum =0
        for key, value in request.POST.items():
                # print(key)
                # print(text_num_split(key))
                value = request.POST[key]
                # print(value)
                if value == '1' :
                    value = int(value)
                    sum += value
        # print('total',sum)
        
        check_StaffID = Staff_Score.objects.filter(Staff = Emp_id, Link_course = Course.objects.get(id = PK_Course_D)).count
        if check_StaffID == 0:
                Staff_prescore_create = Staff_Score(
                                                Pre_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                Pre_Score = sum,
                                                Staff = Staff.objects.get(StaffID = Emp_id),
                                                Link_course = Course.objects.get(id = PK_Course_D)
                                                    )
                Staff_prescore_create.save()
        else : 
            Staff_prescore_update = Staff_Score.objects.get(Staff = Emp_id, Link_course = PK_Course_D)
            Staff_prescore_update.Pre_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Staff_prescore_update.Pre_Score = sum
            Staff_prescore_update.save()

        return redirect('Course_main',PK_Course_D)

    return render(request, 'Pretest.html',{'Profile':Profile, 'Question': Question, 'Course_item':Course_item })

def posttest(request, PK_Course_D):
    Emp_id = request.session['Emp_id']
    Profile ={
        'Fullname' : request.session['Fullname'],
        'Position' : request.session['Position'],
        'LevelCode' : request.session['LevelCode'],
        'Dept' : request.session['Department'],
        'RegionCode' : request.session['RegionCode']
    }
    Course_item = Course.objects.get(id = PK_Course_D)
    Question = Course_Pretest.objects.select_related('Test_Course').filter(Test_Course = Course.objects.get(id = PK_Course_D)).order_by('?')
    # print(Question)
    if request.method == 'POST':
        sum =0
        for key, value in request.POST.items():
                # print(key)
                # print(text_num_split(key))
                value = request.POST[key]
                # print(value)
                if value == '1' :
                    value = int(value)
                    sum += value
        # print('total',sum)
         
        Staff_postscore_update = Staff_Score.objects.get(Staff = Emp_id, Link_course = PK_Course_D)
        Staff_postscore_update.Post_Created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Staff_postscore_update.Post_Score = sum
        Staff_postscore_update.save()

        return redirect('Course_main',PK_Course_D)
    return render(request, 'Posttest.html',{'Profile':Profile, 'Question': Question, 'Course_item':Course_item })

def check_ans(key,value):
    key_cut = key.split("dio")[1]
    # print(key_cut)
    return key_cut

def text_num_split(item):
    for index, letter in enumerate(item, 0):
        if letter.isdigit():
            return [item[:index]]

def errorstage(request):
    mgs = {
                    'massage' : ' '
                }
    if request.method == 'POST':
        Emp_id = request.POST.get('Emp_ID')
        detail = request.POST.get('detail')
        Staff_error_create = Check(
                            Date_check = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            StaffID = Emp_id,
                            Error_Detail = detail
                            )
        Staff_error_create.save()
        return redirect('login')
    
    return render(request,'errorstage.html',{'mgs':mgs})
