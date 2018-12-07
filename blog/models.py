from django.db import models
from django.urls import reverse

from tagging.fields import TagField

# Create your models here.
class CommonModel(models.Model):
    created = models.DateTimeField("Create Date", auto_now_add=True)
    modified = models.DateTimeField("Modify Date", auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)


class Post(CommonModel):
    title = models.CharField('Title', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    tag = TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modified',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modified()

    def get_next_post(self):
        return self.get_next_by_modified()
