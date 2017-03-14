from django.db import models


class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'blog entries'
