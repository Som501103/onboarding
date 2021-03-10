"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from elearning import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^admin/', admin.site.urls),
    url('admin_list_report/', views.admin_list_report, name='admin_list_report'),
    url('home/', views.home, name='home'),
    url('menu/', views.menu, name='menu'),
    url('feedback/', views.feedback, name='feedback'),
    url('ihub_test/', views.ihub_test, name='ihub_test'),
    url('ihub_test_alter/', views.ihub_test_alter, name='ihub_test_alter'),
    url('BU_test/', views.BU_test, name='BU_test'),
    url('virtualclass/', views.virtualclass, name='virtualclass'),
    url('ihub_test_summary/', views.ihub_test_summary, name='ihub_test_summary'),
    path('Course_main/<int:PK_Course_D>/', views.Course_main, name='Course_main'),
    path('ihub_score/<int:Staff_ID>/', views.ihub_score, name='ihub_score'),
    path('VDO/<int:PK_Title>/', views.VDO, name='VDO'),
    path('Pretest/<int:PK_Course_D>/', views.pretest, name='pretest'),
    path('Posttest/<int:PK_Course_D>/', views.posttest, name='posttest'),
    path('evaluate/<int:PK_Course_D>/', views.evaluate, name='evaluate'),
    url('errorstage/',views.errorstage, name='errorstage'),
    path('export/xls/<int:input_course>/', views.export_users_xls, name='export_users_xls'),
]
