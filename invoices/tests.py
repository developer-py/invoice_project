from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-01-04', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.detail_data = {
            'invoice': self.invoice.pk,
            'description': 'Test Description',
            'quantity': 2,
            'unit_price': 10.5,
            'price': 21.0,
        }

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice(self):
        response = self.client.get(f'/invoices/{self.invoice.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        response = self.client.put(f'/invoices/{self.invoice.pk}/', {'date': '2024-01-05', 'customer_name': 'Updated Customer'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        response = self.client.delete(f'/invoices/{self.invoice.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_invoice_detail(self):
        response_invoice = self.client.post('/invoices/', self.invoice_data)
        self.assertEqual(response_invoice.status_code, status.HTTP_201_CREATED)
        created_invoice = Invoice.objects.get(pk=response_invoice.data['id'])
        self.detail_data['invoice'] = created_invoice.pk
        response_detail = self.client.post('/invoice_details/', self.detail_data)
        self.assertEqual(response_detail.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice_detail(self):
        response_invoice = self.client.post('/invoices/', self.invoice_data)
        self.assertEqual(response_invoice.status_code, status.HTTP_201_CREATED)
        created_invoice = Invoice.objects.get(pk=response_invoice.data['id'])
        self.detail_data['invoice'] = created_invoice.pk
        response_detail = self.client.post('/invoice_details/', self.detail_data)
        self.assertEqual(response_detail.status_code, status.HTTP_201_CREATED)
        response_retrieve = self.client.get(f'/invoice_details/{response_detail.data["id"]}/')
        self.assertEqual(response_retrieve.status_code, status.HTTP_200_OK)

    def test_update_invoice_detail(self):
        response_invoice = self.client.post('/invoices/', self.invoice_data)
        self.assertEqual(response_invoice.status_code, status.HTTP_201_CREATED)
        created_invoice = Invoice.objects.get(pk=response_invoice.data['id'])
        self.detail_data['invoice'] = created_invoice.pk
        response_detail = self.client.post('/invoice_details/', self.detail_data)
        self.assertEqual(response_detail.status_code, status.HTTP_201_CREATED)
        updated_data = {
            'description': 'Updated Description',
            'quantity': 3,  
            'unit_price': 15.0,  
            'price': 45.0,  
            'invoice': created_invoice.pk, 
        }
        response_update = self.client.put(f'/invoice_details/{response_detail.data["id"]}/', updated_data)
        print(response_update.data)
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

    def test_delete_invoice_detail(self):
        response_invoice = self.client.post('/invoices/', self.invoice_data)
        self.assertEqual(response_invoice.status_code, status.HTTP_201_CREATED)
        created_invoice = Invoice.objects.get(pk=response_invoice.data['id'])

        self.detail_data['invoice'] = created_invoice.pk
        response_detail = self.client.post('/invoice_details/', self.detail_data)
        self.assertEqual(response_detail.status_code, status.HTTP_201_CREATED)
        response_delete = self.client.delete(f'/invoice_details/{response_detail.data["id"]}/')
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)

