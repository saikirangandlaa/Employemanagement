from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.dateparse import parse_duration

# model for employee table 
class Employe(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=40, null=True, blank=True)
    post = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    employeeid = models.CharField(max_length=40,primary_key=True)
    country = models.CharField(max_length=35, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    active = models.BooleanField(default=True)
    leave_count = models.IntegerField(null=True, blank=True, default=0)
    on_leave = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


# model for Appraisals
class Appraisals(models.Model):
    Name=models.CharField(max_length=35,null=True, blank=True)
    Department=models.CharField(max_length=35,null=True, blank=True)
    performance=models.CharField(max_length=35,null=True, blank=True)
    salary=models.CharField(max_length=35,null=True, blank=True)
    progress=models.CharField(max_length=35,null=True, blank=True)
    feedback=models.CharField(max_length=35,null=True, blank=True)
    hikegot=models.CharField(max_length=35,null=True, blank=True)

    def __str__(self) -> str:
        return self.Name

# model for Timesheets
class Timesheets(models.Model):

    EmoloyeeName=models.CharField(max_length=35,null=True, blank=True)
    department=models.CharField(max_length=100,null=True, blank=True)
    task=models.CharField(max_length=35,null=True, blank=True)
    date=models.DateField(max_length=35,null=True, blank=True)
    timeIn=models.TimeField(max_length=35,null=True, blank=True)
    timeOut=models.TimeField(max_length=35,null=True, blank=True)
    efforts=models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.EmoloyeeName