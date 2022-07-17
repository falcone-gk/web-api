from django.contrib import admin
from projects.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    date_hierarchy = 'created'

admin.site.register(Project, ProjectAdmin)