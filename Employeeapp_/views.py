from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.utils.dateparse import parse_duration
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from .models import *
from django.contrib import messages 



# Create your views here.
#Signup
def sign_up(request):
    if request.method == "POST":
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse("Account Created Successfully!!")
    else:
        frm = SignUpForm()
    return render(request,'signup.html',{'form':frm})


#Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fmr = AuthenticationForm(request=request,data=request.POST)
            if fmr.is_valid():
                uname = fmr.cleaned_data['username']
                upass = fmr.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return HttpResponseRedirect('/home/')
        else:
            fmr = AuthenticationForm()
        return render(request,'userlogin.html',{'form':fmr})
    else:
        return HttpResponseRedirect('/home/')


#Logout
def user_logout(request):
    logout(request)
    return HttpResponse("Logout Successful !!")

#forgotpassword
def forgotpassword(request):      
    return render(request,'forgotpassword.html',{})




#Home Dashboard
@login_required
def home(request):
    em_dta = Employe.objects.filter()
    onn_lve = em_dta.filter(on_leave=True)
    d = {'total_employee':em_dta.count(), 'on_leave':onn_lve.count()}
    return render(request, 'dashboard.html',d)

#creating the employees
@login_required
@staff_member_required
def createEmployeee(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        employeeid = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employe.objects.create(name=name,dob=dob,doj=doj,address=address,employeeid=employeeid,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee created successfully")
        return redirect('employee_list')
    return render(request, 'create_employeee.html')

#listing the employees
@login_required
def employee_list(request):
    em_dta = Employe.objects.filter()
    bit = {'employee':em_dta}
    return render(request, 'employee_list.html',bit)



#editing the employee
@login_required
@staff_member_required
def edit_employee(request, pid):
    em_dta =Employe.objects.get(employeeid=pid)
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        doj = request.POST['doj']
        address = request.POST['address']
        employeeid = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        department = request.POST['department']
        post = request.POST['post']
        emp_obj = Employe.objects.filter(employeeid=pid).update(name=name,dob=dob,doj=doj,address=address,employeeid=employeeid,state=state,zipcode=zipcode,country=country,department=department,post=post)
        messages.success(request, "Employee Updated successfully")
        return redirect('employee_list')
    return render(request, 'edit_employeee.html', {'emp_data':em_dta})

#Deleting of an employee
@login_required
@staff_member_required
def delete_employee(request, pid):
    dta = Employe.objects.get(employeeid=pid)
    dta.delete()
    messages.success(request, "Employee Deleted successfully")
    return redirect('employee_list')

#employee Leaves
@login_required
@staff_member_required
def leave_status(request, pid):
    dta = Employe.objects.get(employeeid=pid)
    if dta.on_leave:
        dta.on_leave = False
    else:
        dta.leave_count = dta.leave_count + 1
        dta.on_leave = True
    dta.save()
    messages.success(request, "Employee leave status Changed successfully.")
    return redirect('employee_list')


# code for appraisal
@login_required
@staff_member_required
def app(request):
    if request.method == "POST":
        Name=request.POST['nm']
        Department=request.POST['d']
        performance=request.POST['p']
        salary=request.POST['s']
        progress=request.POST['pr']
        feedback=request.POST['f']
        hikegot=request.POST['h']
        appr=Appraisals.objects.create(Name=Name,Department=Department,performance=performance,salary=salary,progress=progress,feedback=feedback,hikegot=hikegot)
        # appr.save()
    else:
        return render(request, 'appraisal.html', context={})
    return HttpResponse("Appraisal Added Successfully")


#listing Appraisals
@login_required
@staff_member_required
def appraisal_list(request):
    em_dta = Appraisals.objects.filter()
    bit = {'Appraisal':em_dta}
    return render(request, 'appraisallist.html',bit)

#showing Salary
@login_required
@staff_member_required
def filter_salary(request):
    em_dta = Appraisals.objects.filter()
    bit = {'Appraisal':em_dta}
    return render(request, 'filtersalary.html',bit)


# code for Crerating Timesheets
@login_required
@staff_member_required
def sheets(request):
    if request.method == "POST":
        EmployeeName=request.POST['nm']
        department=request.POST['dep']
        task=request.POST['d']
        date=parse_duration(request.POST['p'])
        timeIn=request.POST['s']
        timeOut=request.POST['to']
        efforts=request.POST['pr']
        ts=Timesheets.objects.create(EmoloyeeName=EmployeeName,department=department,task=task,date=date,timeIn=timeIn,timeOut=timeOut,efforts=efforts)
        ts.save()
    else:
        return render(request, 'timesheets.html', context={})
    return HttpResponse("TIMESHEETS Added Successfully")

#listing of timesheets 
@login_required
def timesheet_list(request):
    em_dta = Timesheets.objects.filter()
    bit = {'timesheets':em_dta}
    return render(request, 'timesheet_list.html',bit)


#pulling all the details of all tables
@login_required
@staff_member_required
def manage_all(request):
    em_dta = Employe.objects.filter()
    em_dta1 = Timesheets.objects.filter()
    em_dta2 = Appraisals.objects.filter()
    bit = {'employee':em_dta,'timesheets':em_dta1,'Appraisal':em_dta2}
    return render(request, 'manage.html',bit)


#listing department
@login_required
def depart(request):
    em_dta = Timesheets.objects.filter()
    bit = {'timesheets':em_dta}
    return render(request, 'department.html',bit)


