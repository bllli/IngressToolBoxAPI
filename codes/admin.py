from django.contrib import admin

from .models import PassCode, Tag


@admin.register(PassCode)
class PassCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'message', 'created', 'checked')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'hide')
    ordering = ('-weight', 'name')
