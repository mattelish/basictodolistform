from django.contrib import admin

# Register your models here.

from .models import Todo

    
class TodoInline(admin.TabularInline):
    model = Todo
    extra = 3

      
class TodoAdmin(admin.ModelAdmin):      
      list_display = ('todo_text', 'created', 'priority', 'difficulty', 'done', 'pub_date', 'was_published_recently')
      model = Todo
      search_fields = ['todo_text']
      list_filter = ['pub_date']
     
      
admin.site.register(Todo, TodoAdmin)