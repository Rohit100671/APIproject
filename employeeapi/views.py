from rest_framework.decorators import api_view
from rest_framework.response import Response

from employeeapi.models import EmployeeAPI
from employeeapi.serializers import Employeeserializer

# Create your views here.
@api_view(['GET', 'POST'])
def giveemployeedata(request):
    return Response({'id':1001,'name':"rohit",'department':"IT",'slary':1500000})

@api_view(['GET'])
def getemployee(request, employeeid):
    employeedb=EmployeeAPI.objects.get(id=employeeid)
    print(employeedb.name)
    # return Response({'id':employeedb.id,'name':employeedb.name,'department':employeedb.department,'salary':employeedb.salary})

    return Response(Employeeserializer(employeedb).data)

@api_view(['GET','POST'])
def addemployee(request):
    dictionary=request.data
    EmployeeAPI.objects.create(id=dictionary['id'], name=dictionary['name'], department=dictionary['department'], salary=dictionary['salary'])
    return Response({'message':'Your Record has been  Submmited'})

@api_view(['PUT'])
def employeeupdate(request):
    dictionary=request.data
    db=EmployeeAPI.objects.get(id=dictionary['id'])
    db.name=dictionary['name']
    db.department=dictionary['department']
    db.salary=dictionary['salary']
    db.save()
    return Response({'meassage':'Recors has been updated'})

@api_view(['DELETE'])
def employeedelete(request,empid):
    dictionary=request.data
    count=EmployeeAPI.objects.filter(id=empid).delete()
    if count[0] == 0:
        return Response({'message':'Recor has not been Exist'})
    
    return Response({'message':'Recor has been Deleted'})