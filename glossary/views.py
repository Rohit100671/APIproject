from rest_framework.response import Response
from rest_framework.decorators import api_view

from glossary.models import Glossary
from glossary.serializers import Glossaryserializer

# Create your views here.
@api_view(['GET', 'POST'])
def showbill(request):
    return Response({'Sr':1,'Item':"Tata Salt",'Quantity':'1kg','Price':"25rs"})


@api_view(['GET', 'POST'])
def getbill(request,srno):
    billdb=Glossary.objects.get(sr=srno)
    # return Response({'SrNo':billdb.sr,'Item':billdb.items,'Quantity':billdb.quantity,'Price':billdb.price})

    return Response(Glossaryserializer(billdb).data)
