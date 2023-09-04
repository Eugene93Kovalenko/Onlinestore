from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from datetime import date
from django.db.models import *

from .models import *
from .utils import DataMixin
from .filters import ProductFilter


class ShopView(DataMixin, ListView):
    model = ProductSizeColor
    template_name = "product_app/shop.html"
    context_object_name = "products"
    paginate_by = 2

    def get_queryset(self):
        if self.request.GET.get("ordering"):
            return ProductSizeColor.objects.filter(self.get_filters()).order_by(
                self.get_ordering()
            )
        return ProductSizeColor.objects.filter(self.get_filters())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["color_list_for_sidebar"] = super().get_color_list()
        context["size_list_for_sidebar"] = super().get_size_list()
        return context | self.get_extra_context()


class HomeView(DataMixin, ListView):
    model = ProductSizeColor
    template_name = "product_app/index.html"
    context_object_name = "products"

    def get_queryset(self):
        return ProductSizeColor.objects.distinct('product_id', 'color_id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["viewed_products"] = Product.objects.all().order_by("-num_visits")[:8]
        if date.today().month in [12, 1, 2]:
            context["selection_name"] = "winter"
            context["next_selection_name"] = "spring"
        elif date.today().month in [3, 4, 5]:
            context["selection_name"] = "spring"
            context["next_selection_name"] = "summer"
        elif date.today().month in [6, 7, 8]:
            context["selection_name"] = "summer"
            context["next_selection_name"] = "autumn"
        else:
            context["selection_name"] = "autumn"
            context["next_selection_name"] = "winter"
        return context | self.get_extra_context()


class ProductView(DataMixin, DetailView):
    model = Product
    template_name = "product_app/product.html"
    context_object_name = "product"
    slug_url_kwarg = "product_slug"

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs["product_slug"])
        # return get_object_or_404(Product, slug=self.kwargs["product_slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_images"] = Product.objects.get(slug=self.kwargs["product_slug"]).images.all()
        return context | self.get_extra_context()   #решить


class CollectionView(DataMixin, ListView):
    model = Product
    template_name = "product_app/shop.html"
    context_object_name = "products"
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(
            Q(collection=self.kwargs["collection_name"]) & Q(self.get_filters())
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        collection_name = self.kwargs["collection_name"]
        context["color_list_for_sidebar"] = super().get_color_list(
            collection_name=collection_name
        )
        context["size_list_for_sidebar"] = super().get_size_list(
            collection_name=collection_name
        )
        return context | self.get_extra_context()


class CategoryView(DataMixin, ListView):
    model = Product
    template_name = "product_app/shop.html"
    context_object_name = "products"
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(
            Q(category__name=self.kwargs["category_name"].title())
            & Q(self.get_filters())
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs["category_name"].title()
        context["color_list_for_sidebar"] = super().get_color_list(category_name=category_name)
        context["size_list_for_sidebar"] = super().get_size_list(category_name=category_name)
        return context | self.get_extra_context()


def contact(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "product_app/contact.html", context)


# class SearchView(DataMixin, ListView):
#     model = Product
#     template_name = 'product_app/shop.html'
#     context_object_name = 'products'
#     paginate_by = 3
#
#     def get_queryset(self):
#         return Product.objects.filter(self.get_filters())
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['color_list_for_sidebar'] = super().get_color_list()
#         context['size_list_for_sidebar'] = super().get_size_list()
#         context['search'] = self.request.GET.get('search')
#         return context | self.get_extra_context()
