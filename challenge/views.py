
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
from django.core import serializers
from user import models
from challenge import models
from django.http import JsonResponse, response
import json

UserModel = auth.get_user_model()

# Create your views here.
#新建题目
@api_view(['POST'])
@permission_classes([AllowAny])
def add_challenge(request):
    data= request.data
    print(data)
    title=data.get("title")
    value_type=data.get("value_type")
    flag=data.get("flag")
    des=data.get("des")
    score=data.get("score")
    c=models.Challenge()
    c.title=title
    c.ChallengeClass=value_type
    c.flag=flag
    c.content=des
    c.initial_points=score
    c.save()
    return Response({"msg":"添加成功"},status=200)

#展示题目
@api_view(['POST'])
@permission_classes([AllowAny])
def show_challenge(request):
    data=request.data
    # print(data)
    type=data.get("type")
    challenges = models.Challenge.objects.filter(ChallengeClass=type).values()
    datas=[]
    for i in challenges:
        # print(i)
        j={"title":i.get("title"),"score":i.get("initial_points"),"solvers":i.get("solved"),"des":i.get("content")}
        # print(j)
        datas.append(j)
    # print(datas)

    return Response({"challenges":datas},status=200)

#提交flag
@api_view(['POST'])
@permission_classes([AllowAny])
def submit_flag(request):
    data=request.data
    print(data)
    user=data.get("user")
    challenge=data.get("cid")
    flag=data.get("flag")
    answer = models.Challenge.objects.filter(title=challenge).values('flag')[0].get("flag")
    #判断是否重复解答
    if models.Solution.objects.filter(title=challenge,nickname=user).count()!=0:
        return Response({"code":700},status=200)


    #解答正确
    if flag==answer:
        s=models.Solution()
        s.nickname=user
        s.title=challenge
        #以下为静态分值，动态分值需修改
        s.points=models.Challenge.objects.filter(title=challenge).values('initial_points')[0].get("initial_points")
        s.save()

        #解答人数+1
        solved=models.Challenge.objects.filter(title=challenge).values('solved')[0].get("solved")+1
        models.Challenge.objects.filter(title=challenge).update(solved=solved)
        return Response({"code":200},status=200)
    else:
        return Response({"code":600},status=200)

    
    