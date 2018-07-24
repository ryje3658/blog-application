from django.contrib import admin
from .models import Post, Category


class PostModelAdmin(admin.ModelAdmin):

	list_display = ["__str__", "created_at"]
	list_filter = ["created_at", "category"]
	search_fields = ["title"]
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)

