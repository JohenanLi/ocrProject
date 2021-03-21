from django.shortcuts import render

# Create your views here.
from .models import Account
from .ser import AccountSerializer

from rest_framework import viewsets,mixins


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class filterAccountList(mixins.ListModelMixin):
    """筛选详情页视图"""
    def get(request):
        user_id = request.GET.get("user_id")
        serializer_class = AccountSerializer
        queryset = Account.objects.filter(user = user_id)
