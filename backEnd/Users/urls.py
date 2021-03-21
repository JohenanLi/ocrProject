from django.urls import path,re_path
from .views import *
urlpatterns = [
    re_path(r'^register/$',UserRegister.as_view()),
    re_path(r'^login/$',UserLogin.as_view()),
    # re_path(r'^list/$',UserInfoList.as_view()),
    path('fetch/',FetchTotalBalance),
    # path('account/',getFilterAccount)
]
