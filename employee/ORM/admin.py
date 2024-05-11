from django.contrib import admin
from .models import Reg_Employee
# Register your models here.


class RegEmployeeAdmin(admin.ModelAdmin):
    # shown required fields on admin site
    list_display = ('name', 'email', 'age', 'gender')


admin.site.register(Reg_Employee, RegEmployeeAdmin)