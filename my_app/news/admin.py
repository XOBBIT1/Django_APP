from django.contrib import admin

from .models import Articles


# Register your models here.
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    model = Articles
    list_display = ("id", "title", "anons", "date")
