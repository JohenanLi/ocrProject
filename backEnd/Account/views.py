from django.shortcuts import render

# Create your views here.
from .models import Account
from .ser import AccountSerializer

from rest_framework import viewsets


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer