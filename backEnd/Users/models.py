from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    id = models.AutoField('用户信息id', primary_key=True)
    username = models.CharField('用户名', unique=True, max_length=20)
    password = models.CharField('密码', max_length=100)
    total_balance = models.FloatField('当前余额', max_length=100,default="0.0")


    def __str__(self):
        return self.username

    def set_password(self,password):
        self.password = make_password(password)
        return None
 
    def check_pwd(self,password):
        return check_password(self.password,password)


# class UserAccount(models.Model):
#     id = models.AutoField('用户与账户id', primary_key=True)
#     user_id = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
#     account_id = models.ForeignKey(to='Account', on_delete=models.CASCADE)
