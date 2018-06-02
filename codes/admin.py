from django.contrib import admin

from .models import PassCode


@admin.register(PassCode)
class PassCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'message', 'created', 'checked')
