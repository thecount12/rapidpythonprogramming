from django.contrib import admin
from blog.models import Comment

# Register your models here.


from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title"]


class CommentAdmin(admin.ModelAdmin):
    def post_name(self, instance):
        return instance.post.title

    list_display = ["author", "post_name"]
    search_fields = ["post_name"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)