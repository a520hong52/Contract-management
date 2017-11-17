#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render, render_to_response,redirect
from django.http import JsonResponse
from .models import ContractAdmin,ContractType
from django.core.paginator import Paginator
from django.core import serializers
from datetime import datetime
import models
import json

def Contract_info_add(request):
    if request.method == 'POST':
        message = {"msg": ""}
        #获取日期范围的值
        date_range = request.POST.get('date-range-picker')
        type_id = request.POST.get('typename')
        workplace_id = request.POST.get('workplace_name')
        #获取form表单提交的可修改的QueryDict数据(.copy)
        form_dict = request.POST.copy()
        print form_dict
        start_end_list = {'start_date':0,'end_date':1}
        #不为空
        if date_range.strip() and type_id.strip() and workplace_id.strip():
            try:
                for key,value in start_end_list.items():
                    #按数据库日期类型格式化获取的日期时间
                    format_date = date_range.split(' - ')[value]
                    start_end_list[key] = format_date
                del form_dict['date-range-picker']
                del form_dict['typename']
                del form_dict['workplace_name']
                form_dict.update(start_end_list)
                form_dict['contract_admin_type_id']=type_id
                form_dict['contract_admin_workplace_id'] = workplace_id
                #form_dict.dict()将QueryDict对象转成dict
                models.ContractAdmin.objects.create(**form_dict.dict())
                message = {"msg": "success"}
                return JsonResponse(message,safe=False)
            except Exception, e:
                message = {"msg": e}
                return JsonResponse(message, safe=False)
    if request.method == 'GET':
        return render_to_response('contract_add.html')

def Contract_tables(request):
    if request.method == 'GET':
        return render(request, 'contract_table.html')
    if request.method == 'POST':
        return render(request, 'contract_table.html')

#通过map函数，将data.values()里面的数据按照format_datetime函数格式化日期时间的值为指定格式，并得到一个新的list列表
#data.values的值是由字典组成的列表
def format_datetime(dic):
    #isinstance()判断变量类型
    if isinstance(dic, dict):
        for x in dic.iteritems():
            key, value = x
            if isinstance(value, datetime):
                dic[key] = value.strftime("%Y-%m-%d %H:%M:%S")
        return dic

#通过map函数，修改字典里面的连表（一对多）的value值为连表的字段值
def do_try(dic):
    dic["contract_admin_type"] = models.ContractType.objects.get(id=dic["contract_admin_type_id"]).typename
    dic['contract_admin_workplace'] = models.Workplace.objects.get(id=dic["contract_admin_workplace_id"]).workplace_name
    return dic

def Getpage(request):
    if request.method == 'GET':
        # 每页多少条数据
        pageSize = int(request.GET.get('pageSize'))
        # 默认从第一页开始
        pageIndex = int(request.GET.get('pageIndex'))-1
        data = models.ContractAdmin.objects.all()
        total = data.count()
        data = data[pageIndex*pageSize:(pageIndex+1)*pageSize]
        return JsonResponse({'total': total, 'rows': map(do_try, map(format_datetime, data.values()))})

def Delete(request):
    if request.method == 'POST':
        message = {"status":""}
        id = request.POST.getlist('id',None)
        if id == None:
            pass
        else:
            try:
                for ids in id:
                    models.ContractAdmin.objects.get(id=ids).delete()
                message = {"status":"success"}
            except Exception, e:
                message = {"status": "数据删除失败"}
        return JsonResponse(message, safe=False)

def Search(request):
    typenameID = request.GET.get('typeName')
    workplace_nameID = request.GET.get('workplaceName')
    search_list = request.GET.get('searchList')
    search_value = request.GET.get('searchText')
    if workplace_nameID == "" and search_value == "" and search_value == "":
        data = models.ContractAdmin.objects.filter(contract_admin_type__id=typenameID)
    if typenameID == "" and search_value == "" and search_value == "":
       data = models.ContractAdmin.objects.filter(contract_admin_workplace__id=workplace_nameID)
    if typenameID == "" and workplace_nameID == "":
        search_type_dic = {
            "name": models.ContractAdmin.objects.filter(name__contains=search_value),
            "company_name": models.ContractAdmin.objects.filter(company_name__contains=search_value),
            "responsible": models.ContractAdmin.objects.filter(responsible__contains=search_value),
            "phone": models.ContractAdmin.objects.filter(phone__contains=search_value),
            "remark": models.ContractAdmin.objects.filter(remark__contains=search_value)
        }
        data = search_type_dic[search_list]
    # 每页多少条数据
    pageSize = int(request.GET.get('pageSize'))
    # 默认从第一页开始
    pageIndex = int(request.GET.get('pageIndex')) - 1
    total = data.count()
    data = data[pageIndex * pageSize:(pageIndex + 1) * pageSize]
    return JsonResponse({'total': total, 'rows': map(do_try, map(format_datetime, data.values()))})

def Update(request):
    if request.method == 'POST':
        message = {"msg":""}
        #获取日期范围的值
        id = request.POST.get('id')
        date_range = request.POST.get('date-range-picker')
        type_id = request.POST.get('typename')
        workplace_id = request.POST.get('workplace_name')
        #获取form表单提交的可修改的QueryDict数据(.copy)
        form_dict = request.POST.copy()
        print form_dict
        start_end_list = {'start_date':0,'end_date':1}
        #不为空
        if date_range.strip() and type_id.strip() and workplace_id.strip():
            try:
                for key,value in start_end_list.items():
                    #按数据库日期类型格式化获取的日期时间
                    format_date = date_range.split(' - ')[value]
                    start_end_list[key] = format_date
                del form_dict['date-range-picker']
                del form_dict['typename']
                del form_dict['workplace_name']
                form_dict.update(start_end_list)
                form_dict['contract_admin_type_id']=type_id
                form_dict['contract_admin_workplace_id'] = workplace_id
                #form_dict.dict()将QueryDict对象转成dict
                models.ContractAdmin.objects.filter(id=id).update(**form_dict.dict())
                message = {"msg": "success"}
                return JsonResponse(message, safe=False)
            except Exception, e:
                message = {"msg": e}
                return JsonResponse(message, safe=False)
