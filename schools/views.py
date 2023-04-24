from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from schools.models import Schools
from schools.serializers import SchoolsSerializer

# Create your views here.

@csrf_exempt
def SchoolsApi(request,id=0):
    if request.method=='GET':
        if id:
           schools= Schools.objects.get(id=id)
           schools_serializer=SchoolsSerializer(schools,many=False)
        else: 
            schools= Schools.objects.all()
            schools_serializer=SchoolsSerializer(schools,many=True)
        return  JsonResponse(schools_serializer.data ,safe=False)
    elif request.method=='POST':
        schools_data= JSONParser().parse(request)
        schools_serializer=SchoolsSerializer(data=schools_data)
        if schools_serializer.is_valid():
            schools_serializer.save()
            return  JsonResponse('Added sucessfully!' ,safe=False)
        return  JsonResponse('Failed to add!' ,safe=False)
    elif request.method=='PUT':
        schools_data= JSONParser().parse(request)
        schools= Schools.objects.get(id=id)
        schools_serializer=SchoolsSerializer(schools,data=schools_data)
        if schools_serializer.is_valid():
            schools_serializer.save()
            return  JsonResponse('Updated sucessfully!' ,safe=False)
        return  JsonResponse('Failed to update!' ,safe=False)



