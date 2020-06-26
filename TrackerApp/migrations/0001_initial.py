# Generated by Django 2.0.5 on 2018-09-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_Name', models.CharField(max_length=25, unique=True)),
                ('Admin_Id', models.CharField(max_length=25, unique=True)),
                ('Password', models.CharField(max_length=25, unique=True)),
                ('Confirm_PassWord', models.CharField(max_length=25, unique=True)),
                ('Email_ID', models.EmailField(max_length=254, unique=True)),
                ('Contact_No', models.IntegerField(unique=True)),
                ('Password_Key', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CounsellorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Counsellor_Name', models.CharField(max_length=25)),
                ('Counsellor_Id', models.CharField(max_length=25, unique=True)),
                ('Password', models.CharField(max_length=25)),
                ('Confirm_PassWord', models.CharField(max_length=25)),
                ('Email_ID', models.EmailField(max_length=254, unique=True)),
                ('Contact_No', models.IntegerField(unique=True)),
                ('Password_Key', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='LeadTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email_ID', models.EmailField(max_length=254, unique=True)),
                ('Contact_No', models.IntegerField(unique=True)),
                ('Enquiry_Date', models.DateField()),
                ('Source_Name', models.CharField(max_length=25)),
                ('Enquired_For', models.CharField(max_length=25)),
                ('Counsellor_Name', models.CharField(max_length=25)),
                ('Course_Fee', models.IntegerField()),
                ('Status', models.CharField(max_length=25)),
                ('Assigned_To', models.CharField(max_length=25)),
                ('Degree', models.CharField(max_length=25)),
                ('YOP', models.DateField()),
                ('Aggregate', models.IntegerField()),
            ],
        ),
    ]
