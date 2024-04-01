from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UsersAPISerializer


class UsersAPI(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UsersAPISerializer(users, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = UsersAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Added new user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_204_NO_CONTENT)
    
    
    def put(self, request):
        user_id = request.data.get('user_id')

        if not User.objects.filter(id=user_id).exists():
            return Response({"error": "User does not exists!"})
        
        instance = User.objects.get(id=user_id)
        serializer = UsersAPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(instance, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request):
        user_id = request.data.get('user_id')

        if not User.objects.filter(id=int(user_id)).exists():
            return Response({"error": "User does not exists!"}, status=status.HTTP_204_NO_CONTENT)
        
        User.objects.get(id=int(user_id)).delete()
        return Response({"status": "Deleted!"}, status=status.HTTP_418_IM_A_TEAPOT)
    
    
