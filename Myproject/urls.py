from django.contrib import admin
from django.urls import path
from mobile import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.Landpage,name='landpage'),
    path('admin/', admin.site.urls),
    path('welcome/',views.Welcome),
    path('runindex/',views.runindex),
    path('aboutus/',views.Aboutus,name='aboutus'),
    path('blog/',views.blog,name='blog'),
    path('getphone/',views.GetphoneMenue,name='getphone'),
    path('invoice/',views.invoice,name="invioce"),
    path('details/',views.Details,name='details'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('checkout/',views.Checkout,name='Checkout'),
    path('auth_login',views.auth_login,name='auth_login'),
    path('auth_register',views.auth_register,name='auth_register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
