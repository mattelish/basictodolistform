from django.contrib import admin

# Register your models here.

from .models import Register

    
class RegisterInline(admin.TabularInline):
    model = Register
    extra = 3

      
class RegisterAdmin(admin.ModelAdmin):      
      list_display = ('First_name','Last_name','Sex','Phone_number','Email','Address','pub_date', 'was_published_recently')
      model = Register
      search_fields = ['First_name']
      list_filter = ['pub_date']
     
      
admin.site.register(Register, RegisterAdmin)
from django.contrib import admin
