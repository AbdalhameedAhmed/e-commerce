from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from .models import Product
from django.urls import reverse_lazy
# Create your views here.
from django.contrib import messages
from django.db import transaction
import pprint

def admin (request):
    return render(request,"products/admin.html")


class GetProductsForProductsPage(ListView):
    model=Product
    template_name="products/products.html"
    context_object_name="products"
    paginate_by = 1
 

class GetProductsForDashboardPage(ListView):
    model=Product
    template_name="products/dashboard.html"
    context_object_name="products"

class UpdateProductView(UpdateView):
    model = Product
    template_name = "products/update.html"
    fields = ['name', 'price', 'image']
    success_url = reverse_lazy('productAdmin')

class DeleteProductView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = reverse_lazy('productAdmin')


class CreateProductView(CreateView):
    model = Product
    template_name = "products/create.html"
    fields = ['name', 'price', 'image']
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

class getProductDetails(DetailView):
    model=Product
    template_name="products/details.html"
    context_object_name="product"
