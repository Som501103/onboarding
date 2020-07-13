from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
import requests, xmltodict
from .models import Staff, Check
import string
from datetime import datetime
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
                else:
                    Staff_score = Staff.objects.get(StaffID = Emp_id)
                    pretest = Staff_score.Score_PreTest
                    print(pretest)
                return redirect('home')
        else:
                mgs = {
                    'massage' : 'รหัสพนักงานหรือรหัสผ่านไม่ถูกต้อง....'
                }
                # return redirect('login',{'mgs':mgs})

    return render(request,'login.html',{'mgs':mgs})

def home(request):
    user_ID = request.session['Emp_id']
    staff_info = idm(user_ID)
    print(staff_info)

    return render(request, 'home.html',{'staff_info':staff_info})

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