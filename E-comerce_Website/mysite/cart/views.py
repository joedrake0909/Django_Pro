from django.shortcuts import render
from django.http import JsonResponse

def cart_add(request):
    print("Add to cart button clicked")
    if request.method=="POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to the cart has an id:",product_id)
        print("Product quantity is ", product_quantity)
    return JsonResponse({'Message': 'Add to cart button clicked'})
