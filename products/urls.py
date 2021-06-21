from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='products'),
    path('<action>/', views.ProductsView.as_view(), name='new-product'),
    path('<action>/<id>', views.ProductsView.as_view(), name='update-product'),
    path('<action>/<id>', views.ProductsView.as_view(), name='delete-product'),
]
