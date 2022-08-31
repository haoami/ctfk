import hashlib
from django.shortcuts import render
import challenge
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,action, throttle_classes
from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
# from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import auth
from django.contrib.auth.models import AbstractUser, User
# from challenge.models import Challenge
# from challenge.models import Solution
from challenge import models as Challengemodels
# from django_vue import user
from team import models as Teammodels
from user import models

from django.http import JsonResponse

UserModel = auth.get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Register
    """
    data= request.data
    print(data)
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    try:
        user = models.BaseUser.objects.create(username=username,password=md5_pwd(password),email=email,nickname=username)
        return Response({"msg":"注册成功"},status=200)
    except:
        return Response({"msg":"用户名已存在"},status=203)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data= request.data
    print(data)
    username = data.get("username")
    password = data.get("password")
    user = models.BaseUser.objects.filter(username=username,password=md5_pwd(password))
    # print(user)

    
    
    if(user.count()==0):
        print("fail")
        return Response({"msg":"登陆失败"},status=201)
    return Response({"msg":"登录成功"},status=200)

# 返回用户信息
@api_view(['POST'])
@permission_classes([AllowAny])
def getuser(request):
    data=request.data
    print(data)
    user=data.get("username")

    web=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Web").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            web=web+x.get("initial_points")
    print(web)

    crypto=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Crypto").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            crypto=crypto+x.get("initial_points")
    print(crypto)

    pwn=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Pwn").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            pwn=pwn+x.get("initial_points")
    print(pwn)

    misc=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Misc").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            misc=misc+x.get("initial_points")
    print(misc)

    reverse=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Reverse").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            reverse=reverse+x.get("initial_points")
    print(reverse)

    android=0
    challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Android").values()
    for x in challenges:
        if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
            android=android+x.get("initial_points")
    print(android)

    total=web+crypto+pwn+misc+reverse+android
    datas=[
    {"type":"Total","score":total},
    {"type":"Web","score":web},
    {"type":"Crypto","score":crypto},
    {"type":"Pwn","score":pwn},
    {"type":"Misc","score":misc},
    {"type":"Reverse","score":reverse},
    {"type":"Android","score":android}]
    return Response({"userdata":datas},status=200)


# 获取用户列表，用于管理员
@api_view(['POST'])
@permission_classes([AllowAny])
def get_users(request):
    users=models.BaseUser.objects.filter().values()
    datas=[]
    for i in users:
        user=i.get("username")
        email=i.get("email")

        #下面这段恶心的代码成因为：我是条懒狗，不想改数据库结构也不想写方法
        web=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Web").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                web=web+x.get("initial_points")
        # print(web)

        crypto=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Crypto").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                crypto=crypto+x.get("initial_points")
        # print(crypto)

        pwn=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Pwn").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                pwn=pwn+x.get("initial_points")
        # print(pwn)

        misc=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Misc").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                misc=misc+x.get("initial_points")
        # print(misc)

        reverse=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Reverse").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                reverse=reverse+x.get("initial_points")
        # print(reverse)

        android=0
        challenges=Challengemodels.Challenge.objects.filter(ChallengeClass="Android").values()
        for x in challenges:
            if Challengemodels.Solution.objects.filter(title=x.get("title"),nickname=user).count()!=0:
                android=android+x.get("initial_points")
        # print(android)

        total=web+crypto+pwn+misc+reverse+android

        isleader=""
        if Teammodels.Relationship.objects.filter(username=user).count()==0:
            isleader="未加入"
        elif Teammodels.Team.objects.filter(team_leader=user).count()==0:
            isleader="队员"
        else:
            isleader="队长"
        j={"username":user,"score":total,"email":email,"job":isleader}
        datas.append(j)
        print(datas)
    return Response({"data":datas},status=200)
        

# 删除用户
@api_view(['POST'])
@permission_classes([AllowAny])
def delete_user(request):
    data=request.data
    print(data)
    username=data.get("username")
    job=data.get("job")
    try:
        if job=="未加入":
            models.BaseUser.objects.filter(username=username).delete()
        elif job=="队员":
            teamname=Teammodels.Relationship.objects.get(username=username).team_name
            models.BaseUser.objects.filter(username=username).delete()
            Teammodels.Relationship.objects.filter(username=username).delete()
            t=Teammodels.Team.objects.get(team_name=teamname)
            t.population=t.population-1
            t.save()
        else:
            teamname=Teammodels.Relationship.objects.get(username=username).team_name
            models.BaseUser.objects.filter(username=username).delete()
            Teammodels.Team.objects.filter(team_leader=username).delete()
            Teammodels.Relationship.objects.filter(team_name=teamname).delete()
        Challengemodels.Solution.objects.filter(nickname=username).delete()
        return Response({"msg":"删除成功"},status=200)
    except:
        return Response({"msg":"删除失败"},status=201)

    


def md5_pwd(pwd:str):#定义一个方函数，传参只能是str类型
    pwd_bytes = pwd.encode()#把传入的密码转换成bytes类型
    jm = hashlib.md5(pwd_bytes)#加密
    print(jm.hexdigest())#返回加密的结果
    return jm.hexdigest()