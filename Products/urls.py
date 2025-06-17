from django.urls import path
from . import views


urlpatterns=[
    path('',views.GetProductsForProductsPage.as_view(),name="products"),
    path('dashboard/',views.GetProductsForDashboardPage.as_view(),name="productAdmin"),
    path('dashboard/create/',views.CreateProductView.as_view(),name="createProduct"),
    path('updateProduct/<int:pk>',views.UpdateProductView.as_view(),name="updateProduct"),
    path('deleteProduct/<int:pk>',views.DeleteProductView.as_view(),name="deleteProduct"),
    path('details/<int:pk>',views.getProductDetails.as_view(),name="productDetails"),
]