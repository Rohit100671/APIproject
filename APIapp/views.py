from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET',"POST"])
def getAPIdata(request):
    return Response({'Name':"Rohit",'Age':21,"Education":"BCA"})

