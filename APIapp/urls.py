from django.urls import path
from APIapp import views
urlpatterns = [
    path('getAPIdata/',views.getAPIdata)
]
