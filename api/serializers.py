from rest_framework.serializers import ModelSerializer
from datetime import datetime

from .models import User


class UsersAPISerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'first_name', 'last_name', 'groups', 'user_permissions', 'date_joined', 'is_superuser']

    def to_representation(self, instance):
        redata = super().to_representation(instance)
        try:
            redata['last_login'] = datetime.strftime(instance.last_login, '%d-%m-%Y %H:%M:%S')
        except:
            redata['last_login'] = datetime.strftime(datetime.now(), '%d-%m-%Y %H:%M:%S')

        return redata
    

