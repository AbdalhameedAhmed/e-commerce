from django.shortcuts import render
from Products.models import Product,Category
from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
# Create your views here.
from django.contrib import messages
from django.db import transaction
# Create your views here.

class GetProductsForDashboardPage(LoginRequiredMixin,ListView):
    model=Product
    template_name="dashboard/dashboard.html"
    context_object_name="products"

def admin (request):
    return render(request,"dashboard/admin.html")

class GetCategoriesForDashboardPage(LoginRequiredMixin,ListView):
    model=Category
    template_name="dashboard/dashboard_categories.html"
    context_object_name="categories"

class UpdateProductView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = "dashboard/update.html"
    fields = ['name','categories', 'price', 'image']
    success_url = reverse_lazy('productAdmin')

class UpdateCategoryView(LoginRequiredMixin,UpdateView):
    model = Category
    template_name = "dashboard/update_category.html"
    fields = ['name']
    success_url = reverse_lazy('categories')

class DeleteProductView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "dashboard/delete.html"
    success_url = reverse_lazy('productAdmin')

class DeleteCategoryView(LoginRequiredMixin,DeleteView):
    model = Category
    template_name = "dashboard/delete_category.html"
    success_url = reverse_lazy('categories')

class DeleteCategoruesView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = "dashboard/delete.html"
    success_url = reverse_lazy('productAdmin')


class CreateProductView(LoginRequiredMixin,CreateView):
    model = Product
    template_name = "dashboard/create.html"
    fields = ['name','categories' ,'price', 'image']
    success_url = reverse_lazy('productAdmin')
    
    def form_valid(self, form):
        try:
            with transaction.atomic():
                # Save the form and get the object
                self.object = form.save()
                messages.success(self.request, 'Product created successfully!')
                return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Error creating product: {str(e)}')
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

class CreateCategoryView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = "dashboard/create_category.html"
    fields = ['name']
    success_url = reverse_lazy('categories')
    
