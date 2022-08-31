
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
# from django_vue import team
from user import models as usermodels
from challenge import models as Challengemodels
from team import models
from django.http import JsonResponse, response
import json

UserModel = auth.get_user_model()

# Create your views here.
#新建战队
@api_view(['POST'])
@permission_classes([AllowAny])
def registerteam(request):
    data=request.data
    print(data)
    teamname=data.get("teamname")
    teamdes=data.get("teamdes")
    logofile=data.get("logofile")
    user=data.get("user")
    t=models.Team()
    t.team_name=teamname
    t.content=teamdes
    t.team_leader=user
    t.logo=logofile
    print(t)
    try:
        t.save()
        r=models.Relationship()
        r.username=user
        r.team_name=teamname
        r.save()
        return Response({"msg":"创建战队成功"},status=200)
    except:
        return Response({"msg":"创建战队失败"},status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def get_team_data(request):
    data=request.data
    print(data)
    teams=models.Team.objects.filter().values()
    datas=[]
    for i in teams:
        score=0
        score=get_team_score(i.get("team_name"))
        j={"teamname":i.get("team_name"),"time":i.get("pub_date"),"teamleader":i.get("team_leader"),"population":i.get("population"),"score":score}
        datas.append(j)
    print(datas)

    return Response({"teams":datas},status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def join_team(request):
    data=request.data
    print(data)
    user=data.get("username")
    teamname=data.get("teamname")
    if user=="":
        print("未登录")
        return Response({"msg":"未登录"},status=200)
    if models.Relationship.objects.filter(username=user).count()!=0:
        print("已经加入过队伍")
        return Response({"msg":"已经加入过队伍"},status=200)
    
    r=models.Relationship()
    r.username=user
    r.team_name=teamname
    r.save()


    t=models.Team.objects.get(team_name=teamname)
    t.population=t.population+1
    t.save()
    return Response({"msg":"加入成功"},status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_team(request):
    try:
        data=request.data
        print(data)
        teamname=data.get("teamname")
        models.Team.objects.filter(team_name=teamname).delete()
        models.Relationship.objects.filter(team_name=teamname).delete()
        return Response({"msg":"删除成功"},status=200)
    except:
        return Response({"msg":"删除失败"},status=201)



def get_team_score(teamname):
    sloved=[]
    score=0
    p=models.Relationship.objects.filter(team_name=teamname).values()
    for i in p:
        user=i.get("username")
        s=Challengemodels.Solution.objects.filter(nickname=user).values()
        for j in s:
            title=j.get("title")
            points=j.get("points")
            if title not in sloved:
                sloved.append(title)
                score=score+points
    return score


@api_view(['POST'])
@permission_classes([AllowAny])
def look_team(request):
    
    data=request.data
    print(data)
    teamname=data.get("teamname")
    datas=show_team_numbers(teamname)
    print(datas)
    return Response({"data":datas},status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def my_team(request):
    data=request.data
    print(data)
    username=data.get("username")
    teamname=models.Relationship.objects.filter(username=username).get().team_name
    res=models.Team.objects.filter(team_name=teamname).get().content
    datas=show_team_numbers(teamname)
    print(datas)
    print(teamname)
    print(res)
    return Response({"teams":datas,"teamname":teamname,"des":res},status=200)


#退队功能，操作人为队长时，可将队员退队，操作人为队员时，可使自己退队
@api_view(['POST'])
@permission_classes([AllowAny])
def leave_team(request):
    data=request.data
    print(data)
    user2=data.get("user1")#操作人
    user1=data.get("user2")#被操作人
    if models.Team.objects.filter(team_leader=user1).count()==1 and user1==user2:
        return Response({"msg":"失败"},status=201)
    
    if models.Team.objects.filter(team_leader=user1).count()==1 and user1!=user2:
        print("flag")
        models.Relationship.objects.filter(username=user2).delete()
        t=models.Team.objects.get(team_leader=user1)
        t.population=t.population-1
        t.save()
        return Response({"msg":"离队操作成功"},status=200)
    elif user1==user2:
        teamname=models.Relationship.objects.filter(username=user2).get().team_name
        models.Relationship.objects.filter(username=user2).delete()
        t=models.Team.objects.get(team_name=teamname)
        t.population=t.population-1
        t.save()
        return Response({"msg":"离队操作成功"},status=200)
    return Response({"msg":"失败"},status=201)




def show_team_numbers(teamname):
    rs=models.Relationship.objects.filter(team_name=teamname).values()
    datas=[]
    for i in rs:
        user=i.get("username")
        email=usermodels.BaseUser.objects.get(username=user).email

        #下面这段恶心的代码的成因为：我是条懒狗，不想改数据库结构也不想写函数
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
        if models.Relationship.objects.filter(username=user).count()==0:
            isleader="未加入"
        elif models.Team.objects.filter(team_leader=user).count()==0:
            isleader="队员"
        else:
            isleader="队长"
        j={"username":user,"email":email,"score":total,"job":isleader}
        datas.append(j)
    return(datas)