import json
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from users.models import Users
from users.serializers import UsersSerializer

# Create your views here.

@csrf_exempt
def UsersApi(request,id=0):
    if request.method=='GET':
        if id:
           users= Users.objects.get(id=id)
           users_serializer=UsersSerializer(users,many=False)
        else: 
            users= Users.objects.all()
            users_serializer=UsersSerializer(users,many=True)
        return  JsonResponse(users_serializer.data ,safe=False)
    elif request.method=='POST':
        users_data= JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return  JsonResponse('Added sucessfully!' ,safe=False)
        return  JsonResponse('Failed to add!' ,safe=False)
    elif request.method=='PUT':
        users_data= JSONParser().parse(request)
        users= Users.objects.get(id=id)
        users_serializer=UsersSerializer(users,data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return  JsonResponse('Updated sucessfully!' ,safe=False)
        return  JsonResponse('Failed to update!' ,safe=False)
    
@csrf_exempt
def Login(request):
    if request.method=='POST':
        body = json.loads(request.body.decode('utf-8'))
        email = body['email']
        password=body['password']
        try:
            users_email = Users.objects.get(email=email)
        except Users.DoesNotExist:
            users_email = None
        if users_email is None:
            return  JsonResponse({'message':'Email not found!','status':'400'} ,safe=False)
        try:
            password_check = Users.objects.get(email=email,password=password)
        except Users.DoesNotExist:
            password_check = None
        if password_check is None:
            return  JsonResponse({'message': 'Incorrect Password','status':'400'}, safe=False)
        users= Users.objects.defer("password").get(email=email,password=password)
        users_serializer=UsersSerializer(users,many=False)
        return  JsonResponse({'status':'200','data':users_serializer.data },safe=False)      


@csrf_exempt
def UsersBySchool(request,id=0):
    if request.method=='GET':
        users= Users.objects.filter(schoolId=id)
        users_serializer=UsersSerializer(users,many=True)
        return  JsonResponse(users_serializer.data ,safe=False)