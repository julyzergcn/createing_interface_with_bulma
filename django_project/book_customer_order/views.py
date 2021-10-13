from django.shortcuts import render


def index(request):
    return render(request, 'dashboard.html')


def book_list(request):
    return render(request, 'books/book_list.html')


def new_book(request):
    return render(request, 'books/new_book.html')


def customer_list(request):
    return render(request, 'customers/customer_list.html')


def order_list(request):
    return render(request, 'orders/order_list.html')
