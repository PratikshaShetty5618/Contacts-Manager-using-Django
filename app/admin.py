from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from import_export.admin import ImportExportModelAdmin

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id','name','gender','email','info','phone') #To display as many cols in start instead of one in __str__
    list_editable = ('info',) #To edit cols in start
    list_display_links = ('id','name')
    list_per_page = 20 
    search_fields = ('name','gender','email','info','phone') #Search based on what cols
    list_filter = ('gender','date_added') #Filter gets added in Side with respective cols

admin.site.register(Contact,ContactAdmin) #Do not Forget to add above class here
admin.site.unregister(Group)