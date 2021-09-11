from django.contrib import admin


from .models import About, Post, PostView, Comment, Like, User

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User)
admin.site.register(About)