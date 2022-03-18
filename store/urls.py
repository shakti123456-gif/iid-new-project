from django.contrib import admin
from django.urls import path, include


from .views import  * 


app_name="store"


urlpatterns = [

     path('',Home.as_view(),name='stores'),
     path('products/<slug>/',ItemDetailView.as_view(),name="products"),
     path('add-to-cart/<slug>/',add_to_cart,name="add-to-cart"),
     path('order-summary',OrderSummaryView.as_view(),name="order-summary"),
     path('remove_item_from_cart/<slug>/',remove_item_from_cart,name="remove_item_from_cart"),
     path('remove-from-cart/<slug>/',remove_from_cart,name="remove"),
     path('myorders/',active_order,name="active_order")


   
]



