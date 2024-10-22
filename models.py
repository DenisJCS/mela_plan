from django.db import models

# Модель для дня недели
class Day(models.Model):
    """Represents a day of the week"""
    name = models.CharField(max_length=20)  # Название дня недели (например, Monday)

    def __str__(self):
        return self.name

# Модель для меню, привязанного к конкретному дню
class Menu(models.Model):
    """Represents a meal for a specific day"""
    day = models.ForeignKey(Day, on_delete=models.CASCADE)  # Привязка к дню недели
    meal_name = models.CharField(max_length=100)  # Название блюда
    description = models.TextField(blank=True)  # Описание блюда (опционально)

    def __str__(self):
        return f"{self.meal_name} for {self.day.name}"
