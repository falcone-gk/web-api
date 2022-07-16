from django.contrib import admin
from projects.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    date_hierarchy = 'created'

admin.site.register(Post, PostAdmin)