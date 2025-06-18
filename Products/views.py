from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Product,Category
from django.urls import reverse_lazy
# Create your views here.
from django.contrib import messages
from django.db import transaction

def admin (request):
    return render(request,"products/admin.html")



class GetProductsForProductsPage(LoginRequiredMixin,ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"
    paginate_by = 1  # Default items per page
    
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



class getProductDetails(LoginRequiredMixin,DetailView):
    model=Product
    template_name="products/details.html"
    context_object_name="product"
