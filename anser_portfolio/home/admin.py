from django.contrib import admin
from home.models import Clients
# Register your models here.

# we can also use decoratror toregister
@admin.register(Clients)

class ClientAdmin(admin.ModelAdmin):
    list_display=('id','c_name','c_email','c_message')
    
# we have registered our model classes
# admin.site.register(Clients,ClientAdmin)