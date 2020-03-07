from django.contrib import admin
from blog.models import Post
from blog.models import Comment
from blog.models import Contact
from models import REG



class PostAdmin(admin.ModelAdmin):
	search_fields=["title"]

class CommentAdmin(admin.ModelAdmin):
	display_fields = ["post", "author", "created"]

class ContactAdmin(admin.ModelAdmin):
	display_fileds=["subject"] 

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(REG)
