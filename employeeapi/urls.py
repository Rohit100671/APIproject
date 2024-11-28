from django.urls import path

from employeeapi import views

urlpatterns = [
    
    path('giveemployeedata/', views.giveemployeedata),
    path('getemployee/<employeeid>', views.getemployee),
    path('addemployee/', views.addemployee),
    path('employeeupdate/', views.employeeupdate),
    path('employeedelete/<empid>', views.employeedelete) 
]
