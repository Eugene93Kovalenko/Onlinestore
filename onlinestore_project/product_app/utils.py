from django.db.models import Q

from .models import *


class DataMixin:
    def get_extra_context(self, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()
        context['gender_categories'] = Category.objects.filter(name__in=['Women', 'Men', 'Kids'])
        context['color_set'] = [product.color for product in self.get_queryset()]
        context['size_set'] = [product.size for product in self.get_queryset()]
        context['count_products'] = self.get_queryset().count()
        context['all_sizes'] = Size.objects.all()
        context['all_colors'] = Color.objects.all()
        context['selected_color'] = [int(num) for num in self.request.GET.getlist('colors')]
        context['selected_size'] = [int(num) for num in self.request.GET.getlist('sizes')]
        if self.request.GET.get('price1') != '0':
            context['selected_price1'] = self.request.GET.get('price1')
        if self.request.GET.get('price2') != '500':
            context['selected_price2'] = self.request.GET.get('price2')
        # context['urlencode'] = self.request.GET.urlencode()
        context['url'] = self.get_urlencode_for_ordering()
        # if self.request.GET.get('search'):
        #     context['search'] = Product.objects.filter(name__icontains=self.request.GET.get('search'))

        # context['form'] = ProductFilterForm()
        return context

    def get_filters(self):
        price_q, color_q, size_q, search_q = Q(), Q(), Q(), Q()

        if self.request.GET.get('price1'):
            min_price, max_price = self.request.GET.get('price1'), self.request.GET.get('price2')
            price_q = Q(price__range=(min_price, max_price))

        for color in self.request.GET.getlist('colors'):
            if color:
                color_q |= Q(color_id=color)

        for size in self.request.GET.getlist('sizes'):
            if size:
                size_q |= Q(size_id=size)

        # if self.request.GET.get('search'):
        #     search_q |= Q(name__icontains=self.request.GET.get('search'))

        return price_q & color_q & size_q

    def get_ordering(self):
        # if self.request.GET.get('ordering') == '-created_at':
        #     return '-created_at'
        # elif self.request.GET.get('ordering') == '-num_visits':
        #     return '-num_visits'
        return self.request.GET.get('ordering')

    def get_urlencode_for_ordering(self):
        urlencode = self.request.GET.urlencode()
        if 'ordering' in urlencode:
            if urlencode.count('=') == 1:
                urlencode = ''
            else:
                urlencode = urlencode[urlencode.find('&') + 1:]
        return urlencode

    def get_color_list(self, collection_name=None, category_name=None):
        count_product_per_color = []
        all_colors = self.get_extra_context()['all_colors']
        color_set = self.get_extra_context()['color_set']
        for color in all_colors:
            if color in color_set:
                if collection_name:
                    count_product_per_color.append(self.get_queryset().filter(color__name=color,
                                                                              collection=collection_name).count())
                elif category_name:
                    count_product_per_color.append(self.get_queryset().filter(color__name=color,
                                                                              category__name=category_name).count())
                else:
                    count_product_per_color.append(self.get_queryset().filter(color__name=color).count())
            else:
                count_product_per_color.append(0)
        color_list_for_sidebar = list(zip(all_colors, count_product_per_color))
        return color_list_for_sidebar

    def get_size_list(self, collection_name=None, category_name=None):
        count_product_per_size = []
        all_sizes = self.get_extra_context()['all_sizes']
        size_set = self.get_extra_context()['size_set']
        for size in all_sizes:
            if size in size_set:
                if collection_name:
                    count_product_per_size.append(self.get_queryset().filter(size__name=size,
                                                                             collection=collection_name).count())
                elif category_name:
                    count_product_per_size.append(self.get_queryset().filter(size__name=size,
                                                                             category__name=category_name).count())
                else:
                    count_product_per_size.append(self.get_queryset().filter(size__name=size).count())
            else:
                count_product_per_size.append(0)
        size_list_for_sidebar = list(zip(all_sizes, count_product_per_size))
        return size_list_for_sidebar


