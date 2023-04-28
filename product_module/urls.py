from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product-list'),
    path('product-favorite', views.AddProductFavorite.as_view(), name='product-favorite'),
    path('<slug>', views.ProductDetailView.as_view(), name='product-detail')
]