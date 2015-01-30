# Register your models here.
from django.contrib import admin
from django.conf import settings

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)
