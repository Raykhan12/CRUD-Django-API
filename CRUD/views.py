from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .models import User
from .serializers import UserSerializer,UserViewSerializer


@api_view(['GET'])
def userlist(request):
    users = User.objects.all()
    serializer = UserViewSerializer(users , many=True)
    return Response(serializer.data)

@api_view(['POST'])    
def createuser(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    return Response({"error":"error"})        

@api_view(['POST'])
def updateUser(request,pk):
    user=User.objects.get(id=pk) 
    serializer = UserSerializer(instance=user,data=request.data)  

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data) 
    return Response({"error":"error"})        

@api_view(['DELETE'])
def deleteUser(request,pk):
    user=User.objects.get(id=pk)
    user.delete()

    return Response('Deleted')