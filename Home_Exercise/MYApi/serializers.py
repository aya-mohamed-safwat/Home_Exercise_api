from rest_framework import serializers
from MYApi.models import Users , Training , Advices


class UserSirializer(serializers.ModelSerializer):
    class Meta:
        model  = Users
        fields ='__all__' 

class TrainingSirializer(serializers.ModelSerializer):
    class Meta:
        model  = Training
        fields = '__all__'


class AdvicesSirializer(serializers.ModelSerializer):
    class Meta:
        model  = Advices
        fields = '__all__'    