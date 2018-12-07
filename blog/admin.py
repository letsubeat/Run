from django.contrib import admin
from blog.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified')
    list_filter = ('modified',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
