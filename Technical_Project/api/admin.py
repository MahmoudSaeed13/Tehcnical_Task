from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'state')


admin.site.register(Task,TaskAdmin)
# Register your models here.
