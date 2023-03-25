from django.shortcuts import render 
from products.models import Product 



# Create your views here.


def get_product(request , slug):
    print('******')
    print(request.user)
    print('******')

    print(request.user.profile.get_cart_count)
    try:
        product = Product.objects.get(slug = slug)
        context = {'product' : product}

        if request.GET.get('size'):
            size = request.GET.get('size')
            quantity = request.GET.get('quantity')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            context['selected_quantity'] = quantity
        print(request)
        return render(request , 'product/product.html' , context = context)
    
    except Exception as e:
        print(e)
        return render(request , 'product/product.html' , context = context)
