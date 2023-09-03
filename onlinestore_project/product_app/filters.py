import django_filters
from .models import *
from django import forms
from .utils import *


class ProductFilter(django_filters.FilterSet):
    color = django_filters.MultipleChoiceFilter(choices=Product.ColorChoices.choices,
                                                widget=forms.CheckboxSelectMultiple)