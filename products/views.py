from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, ProductTagModel, ColorModel


class ProductListView(ListView):
    template_name = 'shop.html'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()

        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__id=tag)

        colors = self.request.GET.get('colors')
        if colors:
            qs = qs.filter(colors_id=colors)

        sort = self.request.GET.get('sort')
        if sort == '-price':
            qs = qs.order_by('-price')
        elif sort == 'price':
            qs = qs.order_by('price')

        return qs

# class ProductDetailView(DetailView):
#     template_name = 'wishlist.html'
#     model = ProductModel
