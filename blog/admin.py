from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # This prepopulates our 'slug' field whilst typing title.
    prepopulated_fields = {'slug': ('title',)}
    # Adds filter feature to filter the list of posts.
    # Filters include status (draft, published) and date created on. 
    list_filter = ('status', 'created_on')
    # Displays post details in row.
    list_display = ('title', 'slug', 'status', 'created_on')
    # Creates a search field for searching posts.
    search_fields = ['title', 'content']
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Displays comment details in a row.
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Add filter to filter comments section.
    # Filters by approved or date created on.
    list_filter = ('approved', 'created_on')
    # Creates a search field for searching comments.
    search_fields = ['name', 'email', 'body']
    # Actions is a dropdown box, default is delete selected items.
    # This takes our 'approve_comments' function as argument.
    actions = ['approve_comments']

    # Added to actions dropdown box.
    def approve_comments(self, request, queryset):
        # Updates approved to True, as default is False.
        queryset.update(approved=True)