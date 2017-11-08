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
                    format_date = datetime.strptime(date_range.split(' - ')[value], "%m/%d/%Y")
                    format_date = datetime.strftime(format_date, "%Y-%m-%d")
                    start_end_list[key] = format_date
                del form_dict['date-range-picker']
                del form_dict['typename']
                del form_dict['workplace_name']
                form_dict.update(start_end_list)
                form_dict['contract_admin_type_id']=type_id
                form_dict['contract_admin_workplace_id'] = workplace_id
                #form_dict.dict()将QueryDict对象转成dict
                models.ContractAdmin.objects.create(**form_dict.dict())
                return JsonResponse("hello,this is a test")
            except Exception, e:
                pass

        else:
            pass
    return render_to_response('contract_add.html')

def Contract_tables(request):
    if request.method == 'POST':
        typenameID = request.POST.get('typename')
        workplace_nameID = request.POST.get('workplace_name')
        search_list = request.POST.get('search_list')
        search_value = request.POST.get('search_text')
        if workplace_nameID == "" and search_value == "":
            data = models.ContractAdmin.objects.filter(contract_admin_type__id = typenameID)
        if typenameID == "" and search_value == "":
            data = models.ContractAdmin.objects.filter(contract_admin_workplace__id = workplace_nameID)
        if typenameID == "" and workplace_nameID == "":
            search_type_dic = {
                "name": models.ContractAdmin.objects.filter(name__contains=search_value),
                "company_name": models.ContractAdmin.objects.filter(company_name__contains = search_value),
                "responsible": models.ContractAdmin.objects.filter(responsible__contains = search_value),
                "phone": models.ContractAdmin.objects.filter(phone__contains=search_value),
                "remark": models.ContractAdmin.objects.filter(remark__contains=search_value)
            }
            if search_list == "":
                pass
            else:
                data = search_type_dic[search_list]

        data = serializers.serialize("json",data)
        print data
        return JsonResponse(data)

    if request.method == 'GET':

        data = models.ContractAdmin.objects.all()
        #每页三条数据，实例化分页对象
        paginator = Paginator(data, 3)
        try:
            #确保页面请求是一个int。 如果没有，请提供第一页。
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
        try:
            #取page页的值的对象
            data = paginator.page(page)
        except:
            #paginator.num_pages 总页数
            #paginator.page(paginator.num_pages)取最后一页的对象
            data = paginator.page(paginator.num_pages)
        print data
        return render(request, 'contract_table.html', {'data': data, 'page': page, 'paginator': paginator})

