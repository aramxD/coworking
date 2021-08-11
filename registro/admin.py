from django.contrib import admin
from .models import *
# Register your models here.


class RegistroAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)


admin.site.register(Registro, RegistroAdmin)