from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users_app.urls', namespace='users_app')),
    # path('checkout/', include('django.contrib.auth.urls')),
    path('', include('product_app.urls', namespace='product_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
