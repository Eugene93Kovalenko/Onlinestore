from django.contrib import admin

from config import settings
from .models import *

admin.site.register(CustomUser)
