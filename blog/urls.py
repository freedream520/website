from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class blogFeed(Feed):
	title = "Blog"
	description = "Some ramblings of mine"
	link = "/blog/feed/"
	
	def items(self):
		return Post.objects.all().order_by("-created")[:5]
	def	item_title(self,item):
		return item.title
	def item_description(self,item):
		return item.body
	def item_link(self,item):
		return u"/blog/%d" % item.id
	

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^$',ListView.as_view(
						queryset=Post.objects.all().order_by("-created")[:5],
						template_name="blog.html")),
	# url(r'^(?P<pk>\d+)$',DetailView.as_view(
							# model=Post,
							# template_name="post.html")),
	url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/(?P<slug>[-\w]+)/$',DetailView.as_view(
							#slug_field='slug',
							model=Post,
							template_name="post.html")),
	url(r'^archives/$',ListView.as_view(
						queryset=Post.objects.all().order_by("-created"),
						template_name="archives.html")),
	url(r'^tag/(?P<tag>\w+)$','tagpage'),
	url(r'^feed/$',blogFeed()),
	)


