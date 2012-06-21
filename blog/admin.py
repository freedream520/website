from django.contrib import admin 
from blog.models import Post

# class postPhotoInline(admin.TabularInline):
	# model = postPhoto

# class postAdmin(VersionAdmin):
	# inlines = [postPhotoInline,]

admin.site.register(Post)
