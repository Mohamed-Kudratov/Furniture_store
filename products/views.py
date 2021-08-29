from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import ProductModel, CategoryModel, ProductTagModel


class ProductListView(ListView):
    template_name = 'shop.html'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
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

        return qs

# class ProductDetailView(DetailView):
#     template_name = 'wishlist.html'
#     model = ProductModel
