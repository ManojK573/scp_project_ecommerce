from django.shortcuts import render
import requests
import json

from . models import Category, Product

from django.shortcuts import get_object_or_404


def store(request):

    response = requests.get('https://sypbxz6e5b.execute-api.us-east-1.amazonaws.com/getproducts')
    all_products = json.loads(response.text)

    context = {'my_products':all_products}

    return render(request, 'store/store.html', context)



def categories(request):

    response = requests.get('https://9bkfrf3v46.execute-api.us-east-1.amazonaws.com/getcategories')
    all_categories = json.loads(response.text)
    

    return {'all_categories': all_categories}



def list_category(request, category_slug=None):

    response = requests.get('https://ltkmmlc1rl.execute-api.us-east-1.amazonaws.com/filterproductsbycategory?category='+str(category_slug))
    products = json.loads(response.text)

    return render(request, 'store/list-category.html', {'category':category_slug,'products':products})



def product_info(request, product_slug):

    response = requests.get('https://1n6atinjh6.execute-api.us-east-1.amazonaws.com/getproductdetails?product='+str(product_slug))
    products = json.loads(response.text)

    context = {'product': products[0]}

    return render(request, 'store/product-info.html', context)







