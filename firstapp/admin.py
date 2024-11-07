from django.contrib import admin
from .models import Employee
from .models import Member

from .models import *

# Register your models here.
admin.site.register(Employee)

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country"

admin.site.register(Member,MemberAdmin)