from django import forms
from django.core import validators
from TrackerApp.models import *

Counsellors = []
data = CounsellorDetails.objects.all()
for i in data:
    Counsellors.append(i.Counsellor_Name)

Counsellor_Choices = [("--Counsellor Name--","--Counsellor Name--"),("ADMIN","admin")]
Status_Choices = [("--Status--","--Status--"),("Lead_in_Followup","Lead_in_Followup"),("Lead_Closed","Lead_Closed"),("Walked-in","Walked-in"),("Registered","Registered"),("Walkedin-closed","Walkedin-closed")]
Field_Choices = [("--Choices to Filter By--","--Choices to Filter By--"),("Name","Name"),("Email_ID","Email_ID"),("Contact_No","Contact_No"),("Enquiry_Date","Enquiry_Date"),("Source_Name","Source_Name"),("Enquired_For","Enquired_For"),("Assigned_To","Assigned_To"),("Degree","Degree"),("YOP","YOP")]

for i in range(0,len(Counsellors)):
    tup = (str(Counsellors[i]),Counsellors[i])
    Counsellor_Choices.append(tup)

Operation_Choices = [("--Operation To Perform--","--Operation To Perform--"),("Update","Update"),("Delete","Delete")]

YOP_Choices = [("--Year of PassedOut--","--Year of PassedOut--"),("2020",2020),("2019",2019),("2018",2018),("2017",2017),("2016",2016),("2015",2015),("2014",2014),("2013",2013),("2012",2012)]

class CounsellorRegister(forms.ModelForm):
    Counsellor_Name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Dont enter in caps... '}))
    Counsellor_Id = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'enter your employee id here... '}))
    Password = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'create password here... '}))
    Confirm_PassWord = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'re-type password... '}))
    Email_ID = forms.EmailField()
    Contact_No = forms.IntegerField()
    Password_Key = forms.CharField()

    class Meta():
        model = CounsellorDetails
        fields="__all__"

class AdminLogin(forms.Form):
    Login_ID = forms.CharField()
    Password = forms.CharField()

class CounsellorLogin(forms.Form):
    Counsellor_Name = forms.CharField(widget=forms.Select(choices=Counsellor_Choices))
    Login_ID = forms.CharField()
    Password = forms.CharField()

class AddLeads(forms.ModelForm):
    Name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'dont enter in caps... '}))
    Email_ID = forms.EmailField()
    Contact_No = forms.IntegerField()
    Counsellor_Name = forms.CharField(widget=forms.Select(choices=Counsellor_Choices))
    Enquiry_Date = forms.DateField(widget= forms.TextInput(attrs={'placeholder':'date format :dd/mm/yyyy'}))
    Source_Name = forms.CharField()
    Enquired_For = forms.CharField()
    Course_Fee = forms.IntegerField()
    Assigned_To =forms.CharField(widget=forms.Select(choices=Counsellor_Choices))
    Degree = forms.CharField()
    YOP = forms.IntegerField(widget=forms.Select(choices=YOP_Choices))
    Aggregate = forms.IntegerField()
    Status = forms.CharField(widget=forms.Select(choices=Status_Choices))

    class Meta():
        model = AddLeads
        fields="__all__"

class FilterLeads(forms.Form):
    Filter_By = forms.CharField(widget=forms.Select(choices=Field_Choices))
    Field_Value = forms.CharField()

class UpdateLeads(forms.Form):
    Search_By = forms.CharField(widget=forms.Select(choices=Field_Choices))
    Field_Value = forms.CharField()
    Operation = forms.CharField(widget=forms.Select(choices=Operation_Choices))

class ViewByCounsellor(forms.Form):
    Counsellor_Name = forms.CharField(widget=forms.Select(choices=Counsellor_Choices))

class CounsellorForm(forms.Form):
    Counsellor_Name = forms.CharField(widget=forms.Select(choices=Counsellor_Choices))
    Password = forms.CharField()

class StatusFilter(forms.Form):
    Status = forms.CharField(widget=forms.Select(choices=Status_Choices))

class StatusForm(forms.Form):
    Status = forms.CharField(widget=forms.Select(choices=Status_Choices))
    Counsellor_Name = forms.CharField(widget=forms.Select(choices=Counsellor_Choices))
    Password = forms.CharField()
