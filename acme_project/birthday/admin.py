from django.contrib import admin
from .models import Tag


admin.site.empty_value_display = 'Не задано'

admin.site.register(Tag)
