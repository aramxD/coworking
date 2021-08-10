from django.contrib import admin
from .models import *
# Register your models here.


class registroAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)


admin.site.register(registro, registroAdmin)