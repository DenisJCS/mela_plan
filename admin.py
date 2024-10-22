from django.contrib import admin
from .models import Day, Menu  # Импортируем обе модели

# Регистрируем модели для отображения в админке
admin.site.register(Day)
admin.site.register(Menu)

