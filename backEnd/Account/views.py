from django.shortcuts import render

# Create your views here.
from .models import Account
from .ser import AccountSerializer

from rest_framework import viewsets,generics


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class filterAccountList(generics.ListAPIView):
    """筛选详情页视图"""
    serializer_class = AccountSerializer
    user_id = 0
    queryset = Account.objects.filter(user = user_id)

    def get(request):
        user_id = request.GET.get("user_id")
        
        # queryset、serializer_class是固定的
        

