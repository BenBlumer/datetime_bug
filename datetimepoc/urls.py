from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:pk>', views.OrderDetailView.as_view(), name='detail'),
    path('create', views.CreateOrderView.as_view(), name='create_order'),
    path('update/<int:pk>', views.CreateOrderView.as_view(), name='update_order'),

]