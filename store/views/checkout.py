from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.payment import Payment


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(phone, customer, cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          phone=phone,
                          rentalTime=cart.get(str(product.id)))

        request.session['cart'] = {}
        return redirect('cart')
