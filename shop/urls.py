from django.urls import path
from .views import SignupView, LoginView, ProductListCreateView, OrderHistoryView, OrderCreateView, product_list_view

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('orders/place/', OrderCreateView.as_view(), name='place-order'),
    path('orders/history/', OrderHistoryView.as_view(), name='order-history'),
    path('products-page/', product_list_view, name='product-list-page'),
]
