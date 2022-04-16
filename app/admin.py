from django.contrib import admin
from .models import App, User, Comment
from django.contrib.auth.admin import Group, UserAdmin

# Register your models here.
admin.site.register(App)
admin.site.unregister(Group)

admin.site.site_header = "Acadship Admin"

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "commenter", "timestamp", "content")

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ("watchlist", )
    fieldsets = UserAdmin.fieldsets + (
        ("Watchlist", {"fields": ("watchlist",)}),
    )

admin.site.register(Comment, CommentAdmin)
admin.site.register(User, CustomUserAdmin)