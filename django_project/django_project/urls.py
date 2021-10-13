from django.contrib import admin
from django.urls import path

from book_customer_order import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="dashboard"),
    path('books/', views.book_list, name="book_list"),
    path('books/new/', views.new_book, name="new_book"),

    path('customers/', views.customer_list, name="customer_list"),

    path('orders/', views.order_list, name="order_list"),

]
