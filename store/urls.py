from django.urls import path
from . import views

urlpatterns = [

    path('', 
         views.home, 
         name='home'),
    
    path('profile/',
         views.profile,
         name='profile'),

    path('order-history/',
         views.order_history,
         name='order_history'),

    path('add-wishlist/<int:id>/',
         views.add_wishlist,
         name='add_wishlist'),

path('wishlist/',
     views.wishlist,
     name='wishlist'),

    path('product/<int:id>/',
         views.product_detail,
         name='product_detail'),

    path('add-to-cart/<int:id>/',
         views.add_to_cart,
         name='add_to_cart'),

    path('cart/',
         views.cart,
         name='cart'),

    path('checkout/',
         views.checkout,
         name='checkout'),
    
    path('add-wishlist/<int:id>/',
         views.add_wishlist,
         name='add_wishlist'),

    path('wishlist/',
        views.wishlist,
        name='wishlist'),

    path('remove-wishlist/<int:id>/',
        views.remove_wishlist,
        name='remove_wishlist'),

    path('buy-now/<int:id>/',
         views.buy_now,
         name='buy_now'),

    path('register/',
         views.register,
         name='register'),

    path('login/',
         views.user_login,
         name='login'),

    path('logout/',
         views.user_logout,
         name='logout'),

]