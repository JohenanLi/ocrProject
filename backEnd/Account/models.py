from django.db import models
from Users.models import UserProfile

# Create your models here.


class Account(models.Model):
    id = models.AutoField("交易id", primary_key=True)
    sum_value = models.FloatField("消费或收入金额", max_length=10)
    date_value = models.DateField('消费日期')
    time_value = models.TimeField('消费时间')
    remarkd_value = models.CharField('备注', max_length=100)
    account_type = models.CharField('消费类型', max_length=20)
    billTypeNumber = models.CharField('简称', max_length=20)
    consumption_or_earn = models.BooleanField('消费或收入')  # 1为收入 #0为支出
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_type
