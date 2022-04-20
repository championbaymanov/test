from django.urls import path
from .views import *

urlpatterns = [
    path('warehouse-list/', WarehouseListAPIView.as_view()),
    
    path('warehouse-super/<int:pk>/', WarehouseSuperAPIView.as_view()),

    path('product-list/', ProductListCreateAPIView.as_view()),

    path('warehouse-create/', WarehouseCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),


    path('customer-list/', CustomerListCreateAPIView.as_view()),
    path('customer/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view()),


    path('delivery-list/', DeliveryListCreateAPIView.as_view()),
    path('delivery/<int:pk>/', DeliveryRetrieveUpdateDestroyAPIView.as_view()),
    # path('warehouse-update/<str:pk>', WarehouseUpdateAPIView.as_view()),
]