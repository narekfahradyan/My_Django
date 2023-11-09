from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('prod/<int:id>/', views.prod, name='prod'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('delete_to_cart', views.delete_to_cart, name='delete_to_cart'),

]