# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from system.storage import FileStorage
from django.db import models

# Create your models here.
class ContractAdmin(models.Model):
    name = models.CharField(max_length=30,verbose_name=u'合同名称')
    company_name = models.CharField(max_length=30,verbose_name=u'供应商名称',null=True,blank=True)
    responsible = models.CharField(max_length=10,verbose_name=u'供应商负责人',null=True,blank=True)
    phone = models.CharField(max_length=13, verbose_name=u'负责人电话',null=True,blank=True)
    #username = models.CharField(max_length=10,verbose_name=u'大道负责人')
    start_date = models.DateField(verbose_name=u'合同开始日期')
    end_date = models.DateField(verbose_name=u'合同结束日期')
    remark = models.CharField(max_length=50,verbose_name=u'备注',null=True,blank=True)
    upload_file = models.FileField(verbose_name=u'文件',upload_to='upload/%Y/%m/%d', storage=FileStorage(),null=True,blank=True)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    change_time = models.DateTimeField(auto_now=True,verbose_name=u'修改时间')

    contract_admin_type = models.ForeignKey('ContractType')
    contract_admin_workplace = models.ForeignKey('Workplace')

    class Meta:
        verbose_name = u'合同名称'
        verbose_name_plural = u'合同名称'

    def __unicode__(self):
        return self.name


class ContractType(models.Model):
    typename = models.CharField(max_length=10,verbose_name=u'合同类型名称')

    class Meta:
        verbose_name = u'合同类型'
        verbose_name_plural = u'合同类型'

    def __unicode__(self):
        return self.typename

class Workplace(models.Model):
    workplace_name = models.CharField(max_length=10,verbose_name=u'职场名称')

    class Meta:
        verbose_name = u'职场名称'
        verbose_name_plural = u'职场名称'

    def __unicode__(self):
        return self.workplace_name