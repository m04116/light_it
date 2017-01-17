from django.db import models
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author) if self.author else self.id


class Comment(MPTTModel):
    parent = TreeForeignKey(
        'self', related_name='children', null=True, db_index=True)

    author = models.ForeignKey('auth.User')
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return str(self.text) if self.text else self.id
