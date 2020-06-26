"""LeadTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import url
from TrackerApp import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.Home,name="Home"),
    url(r'^Home',views.Home,name="Home"),
    url(r'^Admin/',views.AdminLogin,name='Admin'),
    url(r'^CounsellorHome/',views.CounsellorHome,name='CounsellorHome'),
    url(r'^CounsellorLogin/',views.CounsellorLogin,name='CounsellorLogin'),
    url(r'^CounsellorRegister/',views.CounsellorRegister,name='CounsellorRegister'),
    url(r'^AdminDashBoard/',views.AdminDashBoard,name='AdminDashBoard'),
    url(r'^CounsellorDashBoard/',views.CounsellorDashBoard,name='CounsellorDashBoard'),

    url(r'^AddLeads/',views.AddLead,name='AddLeads'),
    url(r'^TrackLeads/',views.TrackLeads,name='TrackLeads'),
    url(r'^FilterLeads/',views.FilterLeads,name='FilterLeads'),
    url(r'^UpdateLeads/',views.UpdateLeads,name='UpdateLeads'),
    url(r'^EditLeads/',views.EditLeads,name='EditLeads'),
    url(r'^ViewByCounsellor/',views.FilterByCounsellor,name='ViewByCounsellor'),
    url(r'^FilterByStatus/',views.FilterByStatus,name='FilterByStatus'),

    url(r'^AddLeads_Counsellor/',views.AddLead_Counsellor,name='AddLeads_Counsellor'),
    url(r'^TrackLeads_Counsellor/',views.TrackLeads_Counsellor,name='TrackLeads_Counsellor'),
    url(r'^FilterLeads_Counsellor/',views.FilterLeads_Counsellor,name='FilterLeads_Counsellor'),
    url(r'^UpdateLeads_Counsellor/',views.UpdateLeads_Counsellor,name='UpdateLeads_Counsellor'),
    url(r'^FilterByStatus_Counsellor/',views.FilterByStatus_Counsellor,name='FilterByStatus_Counsellor'),
]
