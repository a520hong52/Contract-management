# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,verbose_name=u'用户名')
    alias = models.CharField(max_length=20, verbose_name=u'中文名')
    password = models.CharField(max_length=30,verbose_name=u'密码')
    phone = models.CharField(max_length=13,verbose_name=u'手机号码')
    email = models.EmailField(verbose_name=u'邮箱')
    user_info_type = models.ForeignKey('UserType')

    class Meta:
        verbose_name = u'用户名'
        verbose_name_plural = u'用户名'

    def __unicode__(self):
        return self.username


class UserType(models.Model):
    typename = models.CharField(max_length=10,verbose_name=u'用户类型名')

    class Meta:
        verbose_name = u'用户类型名'
        verbose_name_plural = u'用户类型名'

    def __unicode__(self):
        return self.typename