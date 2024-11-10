import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy

from .models import Post
# the feed for searching form us 


class LatestPostsFeed(Feed):
    title = 'My POSTS'
    link = reverse_lazy('BLOG:test')
    description = 'New posts of my POST.'

    def items(self):
        return Post.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
