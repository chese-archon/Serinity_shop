from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.indexpage, name="index"),
    path("home", views.indexpage, name="index"),
    path("home/", views.indexpage, name="index"),
    path("about", views.aboutpage, name="about"),
    path("about/", views.aboutpage, name="about"),
    path("post.html", views.postpage, name="post"),
    path("contact", views.contactpage, name="contact"),
    path("contact/", views.contactpage, name="contact"),

    path("product.html", views.productpage, name="product"),
    #path('product/<int:product_id>', views.productpage, name='product_page'),
    #path('product/<int:product_id>/', views.productpage, name='product_page'),
    path("product", views.productpage, name="product"),
    path("product/", views.productpage, name="product"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)