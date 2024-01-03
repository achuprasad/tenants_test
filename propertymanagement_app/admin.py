from django.contrib import admin

from .models import Property,Unit,TenantProfile,Tenant

# Register your models here.
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(TenantProfile)
admin.site.register(Tenant)