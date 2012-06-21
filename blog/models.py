from django.db import models
from taggit.managers import TaggableManager


# Blog Post
class Post(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	created = models.DateTimeField()
	tags = TaggableManager()
	# photos = models.ManyToManyField(PostPhoto)
	
	def __unicode__(self):
		return self.title



#Photo attached to blog post
# class PostPhoto(models.Model):
	# name = models.CharField(max_length=100)
	# image = models.ImageField(upload_to="postPhotos/%Y/%m/%d",height_field='height',width_field='width')
	# caption = models.CharField(max_length=200)
	# tags = TaggableManager()
	# last_modified = models.DateTimeField(editable=False)
	# created = models.DateTimeField(editable=False)
	# width = models.IntegerField(editable=False)
	# height = models.IntegerField(editable=False)
	# assocPost = models.ForeignKey(Post)
	
	# def __unicode__(self):
		# return self.name





 