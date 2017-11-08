from django.contrib import admin
from login.models import UserInfo,UserType
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(UserType)