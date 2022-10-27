from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at',)
    raw_id_fields = ('author', 'likes', 'tags',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text')
    raw_id_fields = ('author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
