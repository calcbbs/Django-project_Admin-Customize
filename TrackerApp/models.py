from django.db import models

# Create your models here.

class AdminDetails(models.Model):
    Admin_Name = models.CharField(max_length=25,unique=True)
    Admin_Id = models.CharField(max_length=25,unique=True)
    Password = models.CharField(max_length=25,unique=True)
    Confirm_PassWord = models.CharField(max_length=25,unique=True)
    Email_ID = models.EmailField(unique=True)
    Contact_No = models.IntegerField(unique=True)
    Password_Key = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.Admin_Id

class CounsellorDetails(models.Model):
    Counsellor_Name = models.CharField(max_length=25)
    Counsellor_Id = models.CharField(max_length=25,unique=True)
    Password = models.CharField(max_length=25)
    Confirm_PassWord = models.CharField(max_length=25)
    Email_ID = models.EmailField(unique=True)
    Contact_No = models.IntegerField(unique=True)
    Password_Key = models.CharField(max_length=25)

    def __str__(self):
        return self.Counsellor_Id

class AddLeads(models.Model):
    Name = models.CharField(max_length=25)
    Email_ID = models.EmailField(unique=True)
    Contact_No = models.IntegerField(unique=True)
    Counsellor_Name = models.CharField(max_length=25)
    Enquiry_Date = models.DateField()
    Source_Name = models.CharField(max_length=25)
    Enquired_For = models.CharField(max_length=25)
    Course_Fee = models.IntegerField()
    Assigned_To = models.CharField(max_length=25)
    Degree = models.CharField(max_length=25)
    YOP = models.IntegerField()
    Aggregate = models.IntegerField()
    Status = models.CharField(max_length=25)

    def __str__(self):
        return self.Email_ID
