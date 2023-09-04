from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import product_app
from .views import *

app_name = 'product_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug:product_slug>/', ProductView.as_view(), name='product'),
    path('contact/', contact, name='contact'),
    path('collection/<slug:collection_name>/', CollectionView.as_view(), name='collection'),
    path('category/<slug:category_name>/', CategoryView.as_view(), name='category'),

    # path('profile/', AccountView.as_view(), name='account'),
    # path('search/', SearchView.as_view(), name='search'),
]
