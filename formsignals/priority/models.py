from django.db import models
from ..blog.models import BlogEntry


class BlogEntryPriority(models.Model):
    blog_entry = models.OneToOneField(BlogEntry)
    priority = models.BooleanField(help_text='Is this entry high priority?')

    def __str__(self):
        priority_text = 'High' if self.priority else 'Normal'
        return "{priority_text} for {blog_entry}".format(priority_text=priority_text,
                                                         blog_entry=self.blog_entry)

    class Meta:
        verbose_name_plural = 'blog entry priorities'
