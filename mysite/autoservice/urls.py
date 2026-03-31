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
]
