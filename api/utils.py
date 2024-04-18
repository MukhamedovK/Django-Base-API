from rest_framework import status
from django.db.models import Q

from .models import User


def registration_check(formData):
    username = formData.get("username")
    email = formData.get("email")
    password1 = formData.get("password")
    password2 = formData.get("repeat_password")

    if len(password2) < 8:
        return {"error": "Password must be at least 8 characters"}
    if password1 != password2:
        return {"error": "Passwords don't match"}
    if User.objects.filter(email=email).exists():
        return {"error": "Email already taken"}
    if username.isdigit():
        return {"error": "Username mustn't contain only numbers"}
    if User.objects.filter(username=username).exists():
        return {"error": "Username already taken"}

    return None


def login_check(formData, serializerName):
    username = formData.get("username")
    password = formData.get("password")

    if User.objects.filter(Q(username=username) & Q(password=password)).exists():
        logged_user = User.objects.get(username=username)
        serializer = serializerName(logged_user)
        return ({"logged": serializer.data}, status.HTTP_200_OK)

    return ({"error": "Username or password is incorrect!"}, status.HTTP_401_UNAUTHORIZED)


def get_template(request, modelName, serializerName):
    queryset = modelName.objects.all()
    serializer = serializerName(queryset, many=True)
    return serializer.data


def post_template(request, serializerName):
    serializer = serializerName(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return ({"Added new data": serializer.data}, status.HTTP_201_CREATED)
    return ({"error": serializer.errors}, status.HTTP_204_NO_CONTENT)


def put_template(request, modelName, serializerName, data_id):
    if not modelName.objects.filter(id=data_id).exists():
        return ({"error": "Data does not exists!"}, status.HTTP_204_NO_CONTENT)

    instance = modelName.objects.get(id=data_id)
    serializer = serializerName(data=request.data)
    if serializer.is_valid():
        serializer.update(instance, serializer.validated_data)
        return (
            {f"Edited data by id [{data_id}]": serializer.data},
            status.HTTP_205_RESET_CONTENT,
        )

    return (serializer.errors, status.HTTP_400_BAD_REQUEST)


def delete_template(request, modelName, data_id):
    if not modelName.objects.filter(id=data_id).exists():
        return ({"error": "Data does not exists!"}, status.HTTP_204_NO_CONTENT)

    modelName.objects.get(id=data_id).delete()
    return ({"status": f"Deleted data by id [{data_id}]"}, status.HTTP_418_IM_A_TEAPOT)
