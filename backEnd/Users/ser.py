from rest_framework import serializers
from Account.models import Account
from . import  models





class CreateUserSer(serializers.ModelSerializer):
    """新增用户序列化器"""
    password2 = serializers.CharField(max_length=100,write_only=True)
    # mobile = serializers.CharField(max_length=11,min_length=11,write_only=True)
 
    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        if password != password2:
            raise serializers.ValidationError('两次密码不一致，请重新输入！')
        return attrs
 
    # def validate_mobile(self,value):
    #     import re
    #     if not re.match(r'1[3-9]\d{9}',value):
    #         raise serializers.ValidationError('手机号格式不正确请重新输入！')
    #     return value
 
    def create(self, validated_data):
        del validated_data['password2']
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
 
    class Meta:
        model = models.UserProfile
        fields = '__all__'
 
 
class UserInfoSer(serializers.ModelSerializer):
    """用户详情信息序列化器"""
    class Meta:
        model = models.UserProfile
        fields = ('id','username','total_balance')
