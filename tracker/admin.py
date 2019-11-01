from django.contrib import admin
from .models import Homework

# Register your models here.

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'due_date')
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user.id
        super().save_model(request, obj, form, change)
