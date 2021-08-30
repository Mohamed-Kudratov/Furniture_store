from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class CategoryModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductTagModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product tag')
        verbose_name_plural = _('product tags')


class ColorModel(models.Model):
    title = models.CharField(max_length=32, verbose_name=_('color'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _(' color ')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    image_first = models.ImageField(null=True, upload_to='products', verbose_name=_('image first'))
    image_second = models.ImageField(null=True, upload_to='products', verbose_name=_('image second'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveSmallIntegerField(default=0, verbose_name=_('discount'))
    description = models.TextField(verbose_name=_('description'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('category')
    )
    colors = models.ManyToManyField(
        ColorModel,
        related_name='products',
        verbose_name=_('colors')
    )
    tags = models.ManyToManyField(
        ProductTagModel,
        related_name='products',
        verbose_name=_('tags')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_price(self):
        if self.discount:
            return (100 - self.discount) / 100 * self.price
        return self.price

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    # at the moment not necessary
    # def get_related(self):
    #     return self.category.products.order_by('-pk').exclude(id=self.pk)[:3]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
