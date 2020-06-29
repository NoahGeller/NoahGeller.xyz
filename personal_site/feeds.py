from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Post

class BlogFeed(Feed):
    title = 'Noah\'s Blog'
    link = '/blog/'
    description = 'A collection of Noah\'s arbitrary thoughts.'

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('blog:detail', args=[item.slug])
