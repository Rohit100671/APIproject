from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection

from studentapiapp.models import StudentAPI
from studentapiapp.serializers import studentserializer

# Create your views here.
@api_view(['GET', 'POST'])
def giveData(request):
    return Response({'rno':101,'name':"Rohit",'marks':72})

@api_view(['GET','POST'])
def getallstudent(request):
    allstudent=StudentAPI.objects.all()
    alldictionary=studentserializer(allstudent, many=True)
    return Response(alldictionary.data)


@api_view(['GET', 'POST'])
def getstudent(request, rollno):
    studntdb=StudentAPI.objects.get(rno=rollno)
    print(studntdb.name)
    # return Response({'rno':studntdb.rno, 'name':studntdb.name, 'marks':studntdb.marks})
    return Response(studentserializer(studntdb).data)

# TO Insert the New Student in database  with the help of API.
@api_view(['POST'])
def savestudent(request):
    studentdata=request.data
    StudentAPI.objects.create(rno=studentdata["rno"],name=studentdata["name"],marks=studentdata["marks"])
    # print(connection.queries)
    return Response(studentdata)

@api_view(['GET', 'POST'])
def multipledic(request):
    students=request.data
    for student in students:
        StudentAPI.objects.create(rno=student["rno"],name=student["name"],marks=student["marks"])
    # print(connection.queries)
    return Response(students)


@api_view(['put'])
def studentupdate(request):
    dictionary=request.data
    updatedata=StudentAPI.objects.get(rno=dictionary['rno'])
    updatedata.name=dictionary['name']
    updatedata.marks=dictionary['marks']
    # if != dictionary['rno']:
    #     return Response({'message':"Record Not Exist"})
    
    updatedata.save()
    return Response({'message':"Record Updated Successful"})

@api_view(['DELETE'])
def studentdelete(request,rollno):
    count=StudentAPI.objects.filter(rno=rollno).delete()
    if count[0]==0:
        return  Response({'message':"Record Not Exist"})
    
    return Response({'messge':'Rcord Deleted Succssful'})
