from django.contrib import admin
from contract.models import ContractAdmin,ContractType,Workplace
# Register your models here.

admin.site.register(ContractAdmin)
admin.site.register(ContractType)
admin.site.register(Workplace)