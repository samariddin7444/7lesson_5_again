from django.urls import path
from .views import ShopPageView, ShopDetailPageView, ContactPageView, ChackOutPageView, CartPageView, TestimonalPageView, NotFoundPageView, SearchResulPageView

urlpatterns = [
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('shopdetail/', ShopDetailPageView.as_view(), name='detail'),
    path('contact/', ChackOutPageView.as_view(), name='contact'),
    path('cart/', CartPageView.as_view(), name='cart'),
    path('testimonial/', TestimonalPageView.as_view(), name='testimonial'),
    path('checkout/', ChackOutPageView.as_view(), name='checkout'),
    path('notfound/', NotFoundPageView.as_view(), name='notfound'),
    path('search/', SearchResulPageView.as_view(), name='search'),
]

