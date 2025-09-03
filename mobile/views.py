from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import Category,Products,Cart
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import requests
from django.template.loader import render_to_string


# Create your views here.
def ajax_cart_preview(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = cart.get_cart_items()
    else:
        items = []

    html = render_to_string('partials/_cart_preview.html', {'items': items})
    return JsonResponse({'html': html})

def Welcome(request):
    return HttpResponse(' جانقو')

def get_remote_products(request):
    url="https://fakestoreapi.com/products"
    response=requests.get(url)
    data=response.json()
    return JsonResponse(data , safe=False)

def get_remoteproductsview(request):
    url="https://fakestoreapi.com/products"
    response=requests.get(url)
    data=response.json()
    return render(request, 'remoteproducts.html',{"data":data})

def auth_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect("Checkout")
        
    return render(request,"auth/auth_login.html")


@csrf_exempt
def auth_register(request):
    if request.method == "POST":  
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')  
    else:
        form = UserCreationForm()
    return render(request, 'auth/auth_register.html', {'form': form})

def Landpage(request):
    category=Category.objects.all() # قراءة البيانات من الجدول category 
    
    context={
        'data':category
    }
    return render(request,'landpage.html',context)


def Aboutus(request):
    template=loader.get_template('aboutus.html')
    return HttpResponse(template.render())

def blog(request):
    template=loader.get_template('blog.html')
    return HttpResponse(template.render())

def invoice(request):
        if request.method=="POST":
            phone_id=request.POST.get("phone_id")
            full_name=request.POST.get("full_name")
            phone=request.POST.get("phone")
            email=request.POST.get("email")


        phone=[
        {
            "id":"0001",
            "name":"iphone 15 pro",
            "brand":"Apple",
            "price":4599,
            "storge":"255GB",
            "color":"White",
            "image":"images/iphone15.jpg"
        },
         {
            "id":"0002",
            "name":"Galaxy s24 Ultra",
            "brand":"Samsung",
            "price":3999,
            "storge":"255GB",
            "color":"Gray",
            "image":"images/galaxy_s24.jpg"
        },

         {
            "id":"0003",
            "name":"Pixel 8 pro",
            "brand":"Google",
            "price":3299,
            "storge":"255GB",
            "color":"Gray",
             "image":"images/pixel8.jpg"
        },
        {
            "id":"0004",
            "name":"Pixel 8 pro",
            "brand":"Google",
            "price":3299,
            "storge":"255GB",
            "color":"Gray",
             "image":"images/pixel8.jpg"
        },
        
    ]
        
        phones=[p for p in phone if str(p["id"])== str(phone_id)]

        return render(request,"invioce.html",{
            "full_name":full_name,
            "phone":phone,
            "email":email,
            "product":phones
        })

def runindex(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())


@login_required(login_url='auth_login') 
def Checkout(request):
    cart=Cart.objects.select_related("product").all()
   
    context={
        'cart':cart
    }
    
    return render(request,'checkout.html',context)


def GetphoneMenue(request):
    id=request.GET.get("id")
    Product=Products.objects.filter(category_id=id)
    context={
        "product":Product
    }

    return render(request,"phonemenue.html",context)

def Details(request):
     id=request.GET.get("id")
     Product=Products.objects.filter(id=id)
     context={
        "product":Product
    }
     return render(request,"details.html",context)

def add_to_cart(request):
    product_id = request.GET.get("id") 
    
    cart_item,created = Cart.objects.get_or_create(
     product_id=product_id,
     defaults={"quntity":1}
      ) 

    if not created:
        cart_item.quntity += 1
        cart_item.save()

    
    Product=Products.objects.filter(id=product_id)
    context={
        "product":Product
    }
    return render(request,"details.html",context)

def product_list(request):
    products = product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.get_cart_items()
    total = cart.get_cart_total()

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

