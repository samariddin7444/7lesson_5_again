from django.views import View
from django.shortcuts import render, get_object_or_404
from shop.models import Fruit


class ShopPageView(View):
    def get(self, request):
        return render(request, 'shop.html')


class ShopDetailPageView(View):
    def get(self, request):
        return render(request, 'shop-detail.html')


class CartPageView(View):
    def get(self, request):
        return render(request, 'cart.html')


class ChackOutPageView(View):
    def get(self, request):
        return render(request, 'chackout.html')


class TestimonalPageView(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class NotFoundPageView(View):
    def get(self, request):
        return render(request, 'not-found.html')


class SearchResulPageView(View):
    def get(self, request):
        return render(request, 'search.html')


class ContactPageView:
    def get(self, request):
        return render(request, 'contact.html')
