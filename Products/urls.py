from django.urls import path
from . import views


urlpatterns=[
    path('',views.GetProductsForProductsPage.as_view(),name="products"),
    path('details/<int:pk>',views.getProductDetails.as_view(),name="productDetails"),
]