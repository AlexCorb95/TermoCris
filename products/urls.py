from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products import views

urlpatterns = [
    path('create_product/', views.ProductCreateView.as_view(), name='create-product'),
    path('products/', views.ProductListView.as_view(), name='list-of-products')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)