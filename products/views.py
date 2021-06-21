from django.shortcuts import redirect, render
from django.views import View
from products.models import Product
from products.forms import ProductForm

# Create your views here.


class ProductsView(View):

    def get(self, request, action=None, id=None):
        if action == 'new':
            return self.post(request)
        if action == 'update':
            return self.patch(request, id)
        if action == 'delete':
            return self.delete(request, id)

        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})

    def post(self, request, action='new', id=None):
        if id:
            return self.patch(request, id)

        product_form = ProductForm(request.POST or None)

        if product_form.is_valid():
            product_form.save()
            return redirect("products")

        return render(request, "products-form.html", {"product": product_form})

    def patch(self, request, id):
        product_instance = Product.objects.get(id=id)
        product_form = ProductForm(
            request.POST or None, instance=product_instance)

        if product_form.is_valid():
            product_form.save()
            return redirect("products")

        return render(request, "products-form.html", {"product": product_form})

    def delete(self, request, id):
        Product.objects.get(id=id).delete()
        return redirect('products')
