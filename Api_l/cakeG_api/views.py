from django.http import JsonResponse
from django.shortcuts import render
from .models import All_cakes,Occation

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import All_cakesSerializer, OccationSerializer



# Create your views here.
def index(request):
    allcake = All_cakes.objects.all()
    content = {'allcake':allcake,}
    return render(request,'cakeG_api/ALLAPICONTAINER.html',context=content)


@api_view(['GET'])
def getCakeData(request):
    objItems = All_cakes.objects.all()
    serializedcake = All_cakesSerializer(objItems,many=True,context={"request":request}) 
    #in line before this context sends request data in serializers.py so image can get absolute url
    return Response(serializedcake.data)

@api_view(['GET'])
def getOccationData(request):
    objItems = Occation.objects.all()
    serializedoccation = OccationSerializer(objItems,many=True)
    return Response(serializedoccation.data)