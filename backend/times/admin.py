from django.contrib import admin

from times.models import Time


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_time', 'votos', 'created_at', 'ativo')
