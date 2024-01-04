from django.urls import path
from .views import InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView, InvoiceDetailListCreateView, InvoiceDetailRetrieveUpdateDestroyView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name='invoice-retrieve-update-destroy'),
    path('invoice_details/', InvoiceDetailListCreateView.as_view(), name='invoice-detail-list-create'),
    path('invoice_details/<int:pk>/', InvoiceDetailRetrieveUpdateDestroyView.as_view(), name='invoice-detail-retrieve-update-destroy'),
]
