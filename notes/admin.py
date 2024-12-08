from django.contrib import admin

from .models import Note, NoteFile


class NoteFileInLineAdmin(admin.TabularInline):
    model = NoteFile
    fields = ('file',)
    extra = 1


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'text', 'created_time', 'updated_time']
    inlines = (NoteFileInLineAdmin,)


# @admin.register(NoteFile)
# class NoteFileAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Note, NoteAdmin)
from django.contrib import admin

# Register your models here.