from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status , filters
from rest_framework.decorators import api_view
from MYApi.models import Users , Training , Advices
from MYApi.serializers import UserSirializer , TrainingSirializer , AdvicesSirializer



def no_rest(request):
    user =[
        {
            'userId' : 1,
             "name"  : "Aya Mohamed" ,
             "gender": "Female" ,
             "weight": 60 ,
             "height": 165
        }
       ]
    return JsonResponse(user , safe=False)


@api_view(['GET' , 'POST'])
def FBV_List(request):

    if request.method =='GET':
        user = Users.objects.all()
        serializer = UserSirializer(user , many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer =  UserSirializer(data=request.data)
        if serializer.is_vaild():
         serializer.save
         return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def FBV_pk(request,pk ):
   
   user =Users.objects.get(userId=pk)
   
   if request.method =='GET':
        serializer = UserSirializer(user)
        return Response(serializer.data)


   elif request.method == 'PUT':
        serializer =  UserSirializer(user , data=request.data)
        if serializer.is_vaild():
         serializer.save
         return Response(serializer.data )
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


   if request.method =='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_exercise(request):
     if request.method =='GET':
        exercise = Training.objects.all()
        serializer = TrainingSirializer(exercise , many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_advices(request):
   if request.method =='GET':
        advice = Advices.objects.all()
        serializer = AdvicesSirializer( advice , many=True)
        return Response(serializer.data)
