from django.urls import path
from . import views

urlpatterns = [
    
    path('giveData/', views.giveData), 
    path('getstudent/<rollno>', views.getstudent),
    path('getallstudent/', views.getallstudent),
    path('savestudent/', views.savestudent),
    path('multipledic/', views.multipledic),
    path('studentupdate/', views.studentupdate),
    path('studentdelete/<rollno>', views.studentdelete)
]
