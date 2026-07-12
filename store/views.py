from django.shortcuts import render, redirect
from .models import Product, Cart, Order,Wishlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from .models import Wishlist
from django.contrib.auth.decorators import login_required
# HOME PAGE + SEARCH

def home(request):

    search = request.GET.get('search')

    if search:

        products = Product.objects.filter(
            name__icontains=search
        )

    else:

        products = Product.objects.all()


    return render(
        request,
        'home.html',
        {
            'products':products
        }
    )



# PRODUCT DETAILS

def product_detail(request, id):

    product = Product.objects.get(id=id)

    return render(
        request,
        'product_detail.html',
        {
            'product':product
        }
    )



# ADD TO CART
def add_to_cart(request, id):

    product = Product.objects.get(id=id)


    cart, created = Cart.objects.get_or_create(

        user=request.user,

        product=product

    )


    if not created:

        cart.quantity += 1

        cart.save()


    return redirect('cart')
# USER LOGIN

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('home')


    return render(
        request,
        'login.html'
    )



# USER LOGOUT

def user_logout(request):

    logout(request)

    return redirect('user_login')



# CART PAGE

def cart(request):

    items = Cart.objects.all()


    return render(
        request,
        'cart.html',
        {
            'items':items
        }
    )



# ORDER PROCESSING

def checkout(request):

    items = Cart.objects.all()


    for item in items:

        Order.objects.create(

            user=request.user,

            product=item.product,

            amount=item.product.price

        )


    Cart.objects.all().delete()


    return render(
        request,
        'checkout.html'
    )
# USER REGISTRATION

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = UserCreationForm()


    return render(
        request,
        'register.html',
        {'form':form}
    )
# USER LOGIN

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('home')


    return render(
        request,
        'login.html'
    )



# USER LOGOUT

def user_logout(request):

    logout(request)

    return redirect('login')
def buy_now(request, id):

    product = Product.objects.get(id=id)
 

    Order.objects.create(

        user=request.user,

        product=product,

        amount=product.price

    )


    return render(request, 'checkout.html')
# ADD TO WISHLIST
@login_required(login_url='login')
def add_wishlist(request, id):

    product = Product.objects.get(id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect('home')


# VIEW WISHLIST
@login_required(login_url='login')
def wishlist(request):

    items = Wishlist.objects.filter(user=request.user)

    return render(request, 'wishlist.html',
                  {'items': items})

# SHOW WISHLIST
@login_required(login_url='login')
def wishlist(request):

    items = Wishlist.objects.filter(
        user=request.user.id
    )

    return render(
        request,
        'wishlist.html',
        {'items': items}
    )
# REMOVE FROM WISHLIST
def remove_wishlist(request, id):

    item = Wishlist.objects.get(
        id=id,
        user=request.user
    )

    item.delete()

    return redirect('wishlist')
# ORDER HISTORY
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        'order_history.html',
        {'orders': orders}
    )
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    orders_count = Order.objects.filter(user=request.user).count()
    wishlist_count = Wishlist.objects.filter(user=request.user).count()

    return render(request, 'profile.html', {
        'orders_count': orders_count,
        'wishlist_count': wishlist_count
    })