from django.db import models
from taggit.managers import TaggableManager


# Hey Adam! The problem here was that python doesn't have "Foward Declaration"
# You've got to declare classes, methods, etc. before you reference them
# see http://stackoverflow.com/questions/1590608/is-it-possible-to-forward-declare-a-function-in-python
# As you can see, there are ways around that BUT in this case
# Your two objects don't both need to reference each other
# In this configuration, the PostPhoto has a ForeignKey relation to theh Post
# So:
# We can get the Post corresponding to a PostPhoto really easy:
# postPhotoObject.assocPost
# AND we can still get all the PostPhotos corresponding to a Post:
# postObject.postphoto_set.all()
# This is possible due to the implied reverse relationship! Sweet
# See https://docs.djangoproject.com/en/dev/topics/db/queries/ for more such craziness

# Lookin good!

# Blog Post
class Post(models.Model):
	title = models.CharField(max_length = 150)
	body = models.TextField()
	created = models.DateTimeField()
	tags = TaggableManager()
	
	def __unicode__(self):
		return self.title



#Photo attached to blog post
class PostPhoto(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="postPhotos/%Y/%m/%d",height_field='height',width_field='width')
	caption = models.CharField(max_length=200)
	tags = TaggableManager()
	last_modified = models.DateTimeField(editable=False)
	created = models.DateTimeField(editable=False)
	width = models.IntegerField(editable=False)
	height = models.IntegerField(editable=False)
	assocPost = models.ForeignKey(Post)
	
	def __unicode__(self):
		return self.name
