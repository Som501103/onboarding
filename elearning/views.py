from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
import requests, xmltodict
# Create your views here.

def login(request):
    mgs = {
                    'massage' : ' '
                }
    if request.method == 'POST':
        userID = request.POST.get('userID')
        passwordID = request.POST.get('passwordID')
        check_user = Plan_Head.objects.filter(Username = userID, Password = passwordID).count()

        if check_user == 1:
            request.session['userID'] = userID
            return redirect('project_list')
    else: 
        mgs = {
                    'massage' : 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง....'
                }

    return render(request, 'login.html', {'mgs':mgs})
