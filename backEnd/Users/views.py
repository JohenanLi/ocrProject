from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from . import ser
from Account.models import Account

from django.http import HttpResponse,JsonResponse


class UserLogin(APIView):
    '用户登录视图类'
    authentication_classes = []
    # 登录不需要认证

    def post(self, request):
        username = request.POST.get('username').strip()
        pwd = request.POST.get('password').strip()
        if not all([username, pwd]):
            return Response({'msg': '参数不完整', 'code': 400})
        user = UserProfile.objects.filter(username=username).first()
        try:
            user.check_pwd(pwd)
            # 登录成功后生成token
            res = {'msg': 'success', 'code': 200}
            CalcTotalBalance(user)
            res['data'] = ser.UserInfoSer(user).data
            print(res)
        except:
            res = {'msg': '用户名或密码错误', 'code': 404}
        print(res)
        return Response(res)


class UserRegister(CreateAPIView):
    """用户注册视图"""
    authentication_classes = []
    # 用户注册不需要认证
    serializer_class = ser.CreateUserSer


class UserInfoList(ListAPIView):
    """用户详情页视图"""
    serializer_class = ser.UserInfoSer
    queryset = UserProfile.objects.all()


def CalcTotalBalance(userGet):
    allAccounts = Account.objects.filter(user=userGet)
    total_balance: float = 0.0
    for one in allAccounts:
        if one.consumption_or_earn:
            total_balance += one.sum_value
        else:
            total_balance -= one.sum_value
    userGet.total_balance = total_balance
    userGet.save()
    return total_balance


def FetchTotalBalance(request):
    user_id = request.POST.get('user_id')
    userGet = UserProfile.objects.filter(id=user_id).first()
    total_balance = CalcTotalBalance(userGet)
    res = {'total_balance': total_balance}
    return JsonResponse(res,safe=False)

# def getFilterAccount(request):
#     user_id = request.GET.get('user_id')
#     allInfo = requests.get("http://localhost:8000/account/")
#     jsonAll = allInfo.text.strip()
#     print(jsonAll)
#     newList = []
#     for oneInfo in jsonAll:
        
#         print(oneInfo)
#         if oneInfo['user'] == int(user_id):
#             newList.append(oneInfo)
#     print(newList)

def pushImage(request):
    url = 'http://127.0.0.1:8089/api/tr-run/'  # 上传文件接口

    # files = {

    #     'file': ('tst.png',  # 文件名称

    #             open('tst.png', 'rb'),  # 文件路径

    #             'image/png',  # 文件类型

    #             {'Expires': '0'}  # 其他参数,非必传

    #             )

    # }  # => 打开上传文件并且加入文件相关参数



    # data = {

    #     "name": "tst"

    # }
    print(request.FILES)
    file = request.FILES.get("file",None)
    params = {'file':file}

    print(params)
    # data传入请求参数dict,files传入待上传文件参数dict
    import requests,json
    response = requests.post(url, files=params)
    resNew = json.loads(response.text)
    resList = resNew['data']['raw_out']
    with open("dataSet.txt",'w') as f:
        # for one in resList:
        #     print(one)
        #     f.write(one)
        #     f.write('\n')
        # print(resList[0])
        # for one in resList[0]:
        #     print(one)
        for res in resList:
            f.write(res[1] +'\n')
    f.close()
    import re,json,requests
    lines = []
    with open('dataSet.txt', 'r') as file:
        lines = file.readlines()
    file.close()
    date = []
    money = []
    time = []
    cost = []
    nums = []
    types = []
    moneyStr = "\-?\d+\.\d+"
    dateStr = "\d{4}-\d{2}-\d{2}"
    typeStr = "^卡账户.*$"
    timeStr = "\d{2}:\d{2}:\d{2}"
    flag = False
    for i in range(len(lines)):
        res = re.search(dateStr, lines[i])
        if res != None:
            date.append(res[0])
            nums.append(i)

    for j in range(len(nums) - 1):
        for k in range(nums[j], nums[j+1]):
            resMoney = re.search(moneyStr, lines[k])
            resTime = re.search(timeStr, lines[k])
            resType = re.search(typeStr,lines[k])
            if resMoney != None:
                money.append(resMoney[0])
            if resTime != None:
                time.append(resTime[0])
            if resType != None:
                types.append(resType[0])
    for l in range(nums[-1], len(lines)):
        resMoney = re.search(moneyStr, lines[l])
        resTime = re.search(timeStr, lines[l])
        resType = re.search(typeStr, lines[l])
        if resMoney != None:
            money.append(resMoney[0])
        if resTime != None:
            time.append(resTime[0])
        if resType != None:
            types.append(resType[0])

    for i in range(0, len(money), 2):
        cost.append(money[i])

    # print(date,len(date))
    # print(money ,len(money))
    # print(time ,len(time))
    # print(cost,len(cost))
    # print(nums,len(nums))
    minNum = min(len(nums),len(date),len(types),len(time),len(cost))
    for i in range(minNum):
        params = {"sum_value":str(abs(float(cost[i]))),
        "date_value":date[i],
        "time_value":time[i],
        "remarks_value":types[i],
        "account_type":"餐饮伙食",
        "billTypeNumber":"cyhs",
        "consumption_or_earn": 0,
        "user":1
        }
        # params = json.dumps(params)
        # print(params)
        aaa = requests.post("http://localhost:8000/account/",data = params)
    return JsonResponse("{ok:ok}")