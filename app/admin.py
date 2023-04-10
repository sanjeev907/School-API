from django.contrib import admin
from .models import *
from app.models import Price
class SchoolAdmin(admin.ModelAdmin):
    list_display=['Email','Name','City','Pincode','Password']

admin.site.register(School,SchoolAdmin)

class StudentsAdmin(admin.ModelAdmin):
    list_display=['School_name','Name','Grade','Username','Password']

admin.site.register(Students,StudentsAdmin)