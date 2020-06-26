from django.shortcuts import render
from django.http import HttpResponse
from TrackerApp.models import *
from django import forms
from TrackerApp import form

# Create your views here.
def Home(request):
    return render(request,"HomePage.html",{})


#ADMIN OPERATION WILL BE DONE HERE

def AdminLogin(request):
    form_var = form.AdminLogin()

    if(request.method == "POST"):
        form_var = form.AdminLogin(request.POST)
        if(form_var.is_valid()):
            Login_ID1 = request.POST["Login_ID"]
            Password1 = request.POST["Password"]

            data = AdminDetails.objects.filter(Admin_Id=Login_ID1).all()
            for i in data:
                Admin_Id = i.Admin_Id
                Password = i.Password
                if(Admin_Id == Login_ID1 and Password == Password1):
                    count = AddLeads.objects.count()
                    return render(request,"AdminDashBoard.html",{'count':count})
                else:
                    return HttpResponse("The Login ID and Password that you Entered are Wrong")
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AdminLogin.html",{'form':form_var})

    if request.method == 'POST':
            if 'change-password' in request.POST:
                password_message = None
                old_password = request.POST.get('pw')
                new_password = request.POST.get('cpw')
                for  login_row in loginqueryset:
                    if login_row.Userid == int(grandid):
                        if login_row.password == old_password:
                            password_message= "password updated successfully"
                            obj = Login_Table.objects.filter(Userid__iexact = int(grandid)).update(
                                password = new_password
                            )
                        else:
                            password_message= "old password is incorrect"
                        return HttpResponseRedirect("/AdminLogin")

def AdminDashBoard(request):
    return render(request,"AdminDashBoard.html",{})

def AddLead(request):
    form_var = form.AddLeads()
    if(request.method == "POST"):
        form_var = form.AddLeads(request.POST)

        if(form_var.is_valid()):
            form_var.save(commit = True)
            return render(request,"AdminDashBoard.html",{})
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AddLead_Admin.html",{'form':form_var})

def TrackLeads(request):
    data=AddLeads.objects.all()
    return render(request,"TrackLeads_Admin.html",{'form':data})

def FilterLeads(request):
    form_var = form.FilterLeads()
    if(request.method == "POST"):
        form_var = form.FilterLeads(request.POST)

        if(form_var.is_valid()):
            Filter_By = request.POST["Filter_By"]
            Field_Value = request.POST["Field_Value"]

            if(Filter_By == "Name"):
                data = AddLeads.objects.filter(Name=Field_Value).all()
            if(Filter_By == "Email_ID"):
                data = AddLeads.objects.filter(Email_ID=Field_Value).all()
            if(Filter_By == "Contact_No"):
                data = AddLeads.objects.filter(Contact_No=Field_Value).all()
            if(Filter_By == "Enquiry_Date"):
                data = AddLeads.objects.filter(Enquiry_Date=Field_Value).all()
            if(Filter_By == "Source_Name"):
                data = AddLeads.objects.filter(Source_Name=Field_Value).all()
            if(Filter_By == "Enquired_For"):
                data = AddLeads.objects.filter(Enquired_For=Field_Value).all()
            if(Filter_By == "Assigned_To"):
                data = AddLeads.objects.filter(Assigned_To=Field_Value).all()
            if(Filter_By == "Degree"):
                data = AddLeads.objects.filter(Degree=Field_Value).all()
            if(Filter_By == "YOP"):
                data = AddLeads.objects.filter(YOP=Field_Value).all()
            if(Filter_By == "Status"):
                data = AddLeads.objects.filter(Status=Field_Value).all()
            return render(request,"FilterShow_Admin.html",{'form':data})
    return render(request,"FilterLeads.html",{'form':form_var})

def UpdateLeads(request):
    form_var = form.UpdateLeads()
    if(request.method == "POST"):
        form_var = form.UpdateLeads(request.POST)

        if(form_var.is_valid()):
            Search_By = request.POST["Search_By"]
            Field_Value = request.POST["Field_Value"]
            Operation = request.POST["Operation"]

            if(Operation == "Delete"):
                if(Search_By == "Name"):
                    data = AddLeads.objects.filter(Name=Field_Value).delete()
                if(Search_By == "Email_ID"):
                    data = AddLeads.objects.filter(Email_ID=Field_Value).delete()
                if(Search_By == "Contact_No"):
                    data = AddLeads.objects.filter(Contact_No=Field_Value).delete()
                if(Search_By == "Enquiry_Date"):
                    data = AddLeads.objects.filter(Enquiry_Date=Field_Value).delete()
                if(Search_By == "Source_Name"):
                    data = AddLeads.objects.filter(Source_Name=Field_Value).delete()
                if(Search_By == "Enquired_For"):
                    data = AddLeads.objects.filter(Enquired_For=Field_Value).delete()
                if(Search_By == "Assigned_To"):
                    data = AddLeads.objects.filter(Assigned_To=Field_Value).delete()
                if(Search_By == "Degree"):
                    data = AddLeads.objects.filter(Degree=Field_Value).delete()
                if(Search_By == "YOP"):
                    data = AddLeads.objects.filter(YOP=Field_Value).delete()
                if(Search_By == "Status"):
                    data = AddLeads.objects.filter(Status=Field_Value).delete()
                return render(request,"AdminDashBoard.html",{})

            if(Operation == "Update"):
                if(Search_By == "Name"):
                    data = AddLeads.objects.filter(Name=Field_Value).all()
                if(Search_By == "Email_ID"):
                    data = AddLeads.objects.filter(Email_ID=Field_Value).all()
                if(Search_By == "Contact_No"):
                    data = AddLeads.objects.filter(Contact_No=Field_Value).all()
                if(Search_By == "Enquiry_Date"):
                    data = AddLeads.objects.filter(Enquiry_Date=Field_Value).all()
                if(Search_By == "Source_Name"):
                    data = AddLeads.objects.filter(Source_Name=Field_Value).all()
                if(Search_By == "Enquired_For"):
                    data = AddLeads.objects.filter(Enquired_For=Field_Value).all()
                if(Search_By == "Assigned_To"):
                    data = AddLeads.objects.filter(Assigned_To=Field_Value).all()
                if(Search_By == "Degree"):
                    data = AddLeads.objects.filter(Degree=Field_Value).all()
                if(Search_By == "YOP"):
                    data = AddLeads.objects.filter(YOP=Field_Value).all()
                if(Search_By == "Status"):
                    data = AddLeads.objects.filter(Status=Field_Value).all()
                return render(request,"EditLead_Admin.html",{'data':data})

    return render(request,"UpdateLeads.html",{'form':form_var})

def EditLeads(request):
     if request.method=='POST':
        Name1=request.POST['Name']
        Email_ID1=request.POST['Email_ID']
        Contact_No1=request.POST['Contact_No']
        Counsellor_Name1=request.POST['Counsellor_Name']
        Enquiry_Date1=request.POST['Enquiry_Date']
        Source_Name1=request.POST['Source_Name']
        Enquired_For1=request.POST['Enquired_For']
        Course_Fee1=request.POST['Course_Fee']
        Assigned_To1=request.POST['Assigned_To']
        Degree1=request.POST['Degree']
        YOP1=request.POST['YOP']
        Aggregate1=request.POST['Aggregate']
        Status1=request.POST['Status']
        
        data = AddLeads.objects.filter(Email_ID=Email_ID1).update(Name=Name1,Email_ID=Email_ID1,Contact_No=Contact_No1,Counsellor_Name=Counsellor_Name1,Enquiry_Date=Enquiry_Date1,Source_Name=Source_Name1,Enquired_For=Enquired_For1,Course_Fee=Course_Fee1,Assigned_To=Assigned_To1,Degree=Degree1,YOP=YOP1,Aggregate=Aggregate1,Status=Status1)

        return render(request,"AdminDashBoard.html",{})

def FilterByCounsellor(request):
    form_var = form.ViewByCounsellor()
    if(request.method == "POST"):
        form_var = form.ViewByCounsellor(request.POST)

        if(form_var.is_valid()):
            Counsellor_Name1 = request.POST["Counsellor_Name"]
            data = AddLeads.objects.filter(Counsellor_Name=Counsellor_Name1).all()
            return render(request,"FilterShow_Admin.html",{'form':data})
    return render(request,"FilterByCounsellor.html",{'form':form_var})


def FilterByStatus(request):
    form_var = form.StatusFilter()
    if(request.method == "POST"):
        form_var = form.StatusFilter(request.POST)
        if(form_var.is_valid()):
            Status1 = request.POST['Status']
            data = AddLeads.objects.filter(Status=Status1).all()
            return render(request,"FilterShow_Admin.html",{'form':data})
    return render(request,"FilterStatusForm.html",{'form':form_var})


#COUNSELLOR OPERATIONS WILL BE DONE HERE

def CounsellorHome(request):
    return render(request,"CounsellorHome.html",{})

def CounsellorLogin(request):
    form_var = form.CounsellorLogin()

    if(request.method == "POST"):
        form_var = form.CounsellorLogin(request.POST)
        if(form_var.is_valid()):
            Counsellor_Name1 = request.POST["Counsellor_Name"]
            Login_ID1 = request.POST["Login_ID"]
            Password1 = request.POST["Password"]

            data = CounsellorDetails.objects.filter(Counsellor_Id=Login_ID1).all()
            for i in data:
                Counsellor_Id = i.Counsellor_Id
                Password = i.Password
                if(Counsellor_Id == Login_ID1 and Password == Password1):
                    return CounsellorDashBoard(request)
                else:
                    return HttpResponse("The Login ID and Password that you Entered are Wrong")
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"CounsellorLogin.html",{'form':form_var})

def CounsellorRegister(request):
    form_var = form.CounsellorRegister()

    if(request.method == "POST"):
        form_var = form.CounsellorRegister(request.POST)

        if(form_var.is_valid()):
            form_var.save(commit = True)
            return render(request,"CounsellorDashBoard.html",{})
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"CounsellorRegister.html",{'form':form_var})



def CounsellorDashBoard(request):
    return render(request,"CounsellorDashBoard.html",{})



def AddLead_Counsellor(request):
    form_var = form.AddLeads()

    if(request.method == "POST"):
        form_var = form.AddLeads(request.POST)

        if(form_var.is_valid()):
            form_var.save(commit = True)
            return render(request,"CounsellorDashBoard.html",{})
        else:
            return HttpResponse("The form fields are not valid")
    return render(request,"AddLead_Counsellor.html",{'form':form_var})

def TrackLeads_Counsellor(request):
    form_var = form.CounsellorForm()
    if(request.method == "POST"):
        form_var = form.CounsellorForm(request.POST)
        if(form_var.is_valid()):
            Counsellor_Name1 = request.POST["Counsellor_Name"]
            Password1 = request.POST["Password"]
            data = CounsellorDetails.objects.filter(Counsellor_Name=Counsellor_Name1).all()
            for i in data:
                Counsellor_Name2 = i.Counsellor_Name
                Password2 = i.Password
                if(Counsellor_Name1 == Counsellor_Name2 and Password1 == Password2):
                    data = AddLeads.objects.filter(Counsellor_Name=Counsellor_Name1).all()
                    return render(request,"TrackLead_Counsellor.html",{'form':data})
    return render(request,"FormShow.html",{'form':form_var})

def FilterLeads_Counsellor(request):
    form_var = form.FilterLeads()
    form_var2 = form.CounsellorForm()
    if(request.method == "POST"):
        form_var = form.FilterLeads(request.POST)
        form_var2 = form.CounsellorForm(request.POST)

        if(form_var.is_valid() and form_var2.is_valid()):
            Filter_By = request.POST["Filter_By"]
            Field_Value = request.POST["Field_Value"]

            Counsellor_Name1 = request.POST["Counsellor_Name"]
            Password1 = request.POST["Password"]
            data = CounsellorDetails.objects.filter(Counsellor_Name=Counsellor_Name1).all()
            for i in data:
                Counsellor_Name2 = i.Counsellor_Name
                Password2 = i.Password
                if(Counsellor_Name1 == Counsellor_Name2 and Password1 == Password2):
                    if(Filter_By == "Name"):
                        data = AddLeads.objects.filter(Name=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Email_ID"):
                        data = AddLeads.objects.filter(Email_ID=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Contact_No"):
                        data = AddLeads.objects.filter(Contact_No=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Enquiry_Date"):
                        data = AddLeads.objects.filter(Enquiry_Date=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Source_Name"):
                        data = AddLeads.objects.filter(Source_Name=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Enquired_For"):
                        data = AddLeads.objects.filter(Enquired_For=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Assigned_To"):
                        data = AddLeads.objects.filter(Assigned_To=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Degree"):
                        data = AddLeads.objects.filter(Degree=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "YOP"):
                        data = AddLeads.objects.filter(YOP=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    if(Filter_By == "Status"):
                        data = AddLeads.objects.filter(Status=Field_Value,Counsellor_Name=Counsellor_Name1).all()
                    return render(request,"TrackLead_Counsellor.html",{'form':data})
    return render(request,"FormShow2.html",{'form':form_var,'form1':form_var2})

def UpdateLeads_Counsellor(request):
    form_var = form.UpdateLeads()
    if(request.method == "POST"):
        form_var = form.UpdateLeads(request.POST)

        if(form_var.is_valid()):
            return HttpResponse("Update leads")
    return render(request,"FormShow.html",{'form':form_var})

def FilterByStatus_Counsellor(request):
    form_var = form.StatusForm()
    if(request.method == "POST"):
        form_var = form.StatusForm(request.POST)
        if(form_var.is_valid()):
            Status1 = request.POST['Status']
            Counsellor_Name1 = request.POST['Counsellor_Name']
            Password1 = request.POST['Password']
            data = CounsellorDetails.objects.filter(Counsellor_Name=Counsellor_Name1).all()
            for i in data:
                Counsellor_Name2 = i.Counsellor_Name
                Password2 = i.Password
                if(Counsellor_Name1 == Counsellor_Name2 and Password1 == Password2):
                    data1 = AddLeads.objects.filter(Counsellor_Name=Counsellor_Name1,Status=Status1).all()
                    return render(request,"TrackLead_Counsellor.html",{'form':data1})
    return render(request,"FormShow.html",{'form':form_var})
