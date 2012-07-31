from django.contrib import admin 
from blog.models import Post,PostPhoto

class postPhotoInline(admin.TabularInline):
	model = PostPhoto

class postAdmin(admin.ModelAdmin):
	inlines = [postPhotoInline,]
	#prepopulated_fields = {"slug" : ('created',)}

admin.site.register(Post)
