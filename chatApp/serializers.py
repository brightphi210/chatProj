
from rest_framework.serializers import ModelSerializer
from . models import *

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomSerializerExist(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class RoomSerializerGet(ModelSerializer):
    messages = MessageSerializer(many=True)
    class Meta:
        model = Room
        fields = '__all__'