#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render, render_to_response,redirect
from django.http.response import HttpResponse
from .models import UserInfo
import models
import json

# Create your views here.
def Login(request):
    if request.method == 'POST':
        status = {'msg': ''}
        #获取表单里面的输入的用户名和密码值
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        empty = all([username,password])
        if empty:
            #这里的models必须引入app的models文件里面的UserInfo类
            count = models.UserInfo.objects.filter(username = username,password = password).count()
            if count == 1:
                return redirect('/index/',content_type='application/json')
            else:
                status['msg'] = "用户名密码错误"
                return HttpResponse(json.dumps(status))

        else:
            status['msg'] = "用户名和密码不能为空"
            return HttpResponse(json.dumps(status))
    return render_to_response('login.html')
def Index(request):
    if request.method == 'POST':
        return render_to_response('index.html')

    if request.method == 'GET':
        return render_to_response('index.html')

