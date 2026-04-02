from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_pk>/', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name="order"),
    path('search/', views.search, name='search'),
    path('userorders/', views.UserOrderListView.as_view(), name="user_orders"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name="profile"),
    path('orders/create/', views.OrderCreateView.as_view(), name="order_create"),
    path("orders/<int:pk>/update/", views.OrderUpdateView.as_view(), name='order_update'),
    path("orders/<int:pk>/delete/", views.OrderDeleteView.as_view(), name='order_delete'),
    path('orders/<int:pk>/createorderline/', views.OrderLineCreateView.as_view(), name="orderline_create"),
    path("orderlines/<int:pk>/update/", views.OrderLineUpdateView.as_view(), name="orderline_update"),
    path("orderlines/<int:pk>/delete/", views.OrderLineDeleteView.as_view(), name="orderline_delete"),
]
