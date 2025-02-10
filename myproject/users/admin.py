
from django.contrib import admin
# from django.contrib.auth.models import User  # Удалите, если не нужно

# Удалите или закомментируйте admin.site.register(User), так как модель уже зарегистрирована

from .models import Application  # Импортируем модель заявки

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'created_at')  # Поля, которые будут отображаться в списке
    search_fields = ('email', 'phone')  # Поля, по которым можно искать
    list_filter = ('created_at',)  # Фильтр по дате создания

# Или можно использовать admin.site.register(Application) без декоратора
