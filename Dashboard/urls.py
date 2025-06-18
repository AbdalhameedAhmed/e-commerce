from django.urls import path
from . import views
urlpatterns = [

path('',views.GetProductsForDashboardPage.as_view(),name="productAdmin"),
    path('create/',views.CreateProductView.as_view(),name="createProduct"),
    path('categories/',views.GetCategoriesForDashboardPage.as_view(),name="categories"),
    path('categories/create',views.CreateCategoryView.as_view(),name="createcategory"),
    path('updateProduct/<int:pk>',views.UpdateProductView.as_view(),name="updateProduct"),
    path('updateCategory/<int:pk>',views.UpdateCategoryView.as_view(),name="updateCategory"),
    path('deleteProduct/<int:pk>',views.DeleteProductView.as_view(),name="deleteProduct"),
    path('deleteCategory/<int:pk>',views.DeleteCategoryView.as_view(),name="deleteCategory"),
]