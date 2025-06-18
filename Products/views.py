from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from django.db.models import Q
from .models import Product,Category
from django.urls import reverse_lazy
# Create your views here.
from django.contrib import messages
from django.db import transaction

def admin (request):
    return render(request,"products/admin.html")


# class GetProductsForProductsPage(ListView):
#     model=Product
#     template_name="products/products.html"
#     context_object_name="products"
#     paginate_by = 3
#     extra_context = {
#         'categories': Category.objects.all()
#     }

class GetProductsForProductsPage(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"
    paginate_by = 3  # Default items per page
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Get all filter parameters from request
        params = {
            'search': self.request.GET.get('search'),
            'category': self.request.GET.get('category'),
            'items': self.request.GET.get('items')
        }
        # Apply search filter (name only as per your model)
        if params['search']:
            queryset = queryset.filter(name__icontains=params['search'])
        
        # Apply category filter
        if params['category']:
            queryset = queryset.filter(categories__name=params['category'])
        
        # Update pagination size
        if params['items'] and params['items'].isdigit():
            self.paginate_by = int(params['items'])
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add all categories to context
        context['categories'] = Category.objects.all().distinct()
        
        # Preserve current filter values
        context['current_filters'] = {
            'search_query': self.request.GET.get('search', ''),
            'category_query': self.request.GET.get('category', ''),
            'items_query': self.paginate_by
        }
        
        
        return context

class GetProductsForDashboardPage(ListView):
    model=Product
    template_name="products/dashboard.html"
    context_object_name="products"

class UpdateProductView(UpdateView):
    model = Product
    template_name = "products/update.html"
    fields = ['name','categories', 'price', 'image']
    success_url = reverse_lazy('productAdmin')

class DeleteProductView(DeleteView):
    model = Product
    template_name = "products/delete.html"
    success_url = reverse_lazy('productAdmin')


class CreateProductView(CreateView):
    model = Product
    template_name = "products/create.html"
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

class getProductDetails(DetailView):
    model=Product
    template_name="products/details.html"
    context_object_name="product"
