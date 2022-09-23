from django.contrib import admin

# Register your models here.
from . models import Post, Author, Tag, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

    list_display = ["title", "author", "status"]
    list_filter = ("status",)
    search_fields = ['title', 'description']


admin.site.register(Author)
admin.site.register(Tag)
