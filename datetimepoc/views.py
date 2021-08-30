from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse
from .models import Order
from .forms import NewOrderForm

class CreateOrderView(generic.CreateView):
    model = Order
    template_name = "datetimepoc/create_order.html"
    form_class = NewOrderForm
    def get_success_url(self):
        return reverse('datetimepoc/index')

class UpdateOrderView(generic.UpdateView):
    model = Order
    fields = "__all__"
    template_name = "datetimepoc/create_order.html"
    form_class = NewOrderForm

    def get_success_url(self):
        return reverse('datetimepoc/list_orders')

class OrderDetailView(generic.DetailView):
    template_name = "datetimepoc/order_detail.html"
    model = Order
