from django.urls import path

from glossary import views

urlpatterns = [
    
    path('showbill/', views.showbill),
    path('getbill/<srno>', views.getbill)
]
