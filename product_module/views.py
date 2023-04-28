from django.shortcuts import redirect
from .models import Product
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView



class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['favorite_product'] = product.id
        return redirect(product.get_absolute_url())


class ProductDetailView(DetailView):
    template_name = 'product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_product = self.object
        favorite_product_id = self.request.session.get('favorite_product')
        context['is_favorite'] = favorite_product_id == loaded_product.id
        return context


class ProductsListView(ListView):
    template_name = 'products_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 1















