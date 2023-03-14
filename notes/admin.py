from django.contrib import admin
from . import models


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created')


admin.site.register(models.Notes, NotesAdmin)
