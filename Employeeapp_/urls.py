from django.contrib import admin
from django.urls import path
from Employeeapp_ import views
urlpatterns = [
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword1'),
    path('addappraisal/',views.app, name="appraisal1"),
    path('timesheets/',views.sheets, name="timesheets1"),
    path('home/',views.home, name="home"),
    path('create-employee',views.createEmployeee, name="create_employee"),
    path('employee-list',views.employee_list, name="employee_list"),
    path('appraisal-list',views.appraisal_list, name="appraisal_list"),
    path('department-list',views.depart, name="department_list"),
    path('timesheet-list',views.timesheet_list, name="timesheet_list"),
    path('filter-salary',views.filter_salary, name="filter_salary"),
    path('manage-list',views.manage_all, name="manage_list"),
    path('employee-edit/<int:pid>',views.edit_employee, name="edit_employee"),
    path('delete-employee/<int:pid>',views.delete_employee, name="delete_employee"),
    path('leave-status/<int:pid>',views.leave_status, name="leave_status"),

]