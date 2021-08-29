from django.db import models
from django.utils.translation import gettext as _


class PostTagModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=225, verbose_name=_('title'))
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    context = models.TextField(null=True, verbose_name=_('context'))
    tags = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('post'))
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
