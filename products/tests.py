from django.test import TestCase
from products.models import Product
import pytest


class TestModels:

    @pytest.mark.django_db
    def test_product_post_model():
        product = Product.objects.create(
            name='Teste',
            description='produto teste',
            price=50.00,
        )
        assert product.id == 1


class TestViews(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Teste',
            description='produto teste',
            price=50.00,

        )
        self.product_to_create = {
            'name': 'Teste2',
            'description': 'produto teste2',
            'price': 100,
        }
        self.product_to_edit = {
            'name': 'Teste atualizado',
        }

    def test_get_list_product_api(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_get_post_product_api(self):
        response = self.client.get('/products/new/')
        self.assertEqual(response.status_code, 200)

    def test_get_patch_product_api(self):
        response = self.client.get(f'/products/update/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_get_delete_product_api(self):
        response = self.client.get(f'/products/delete/{self.product.id}')
        self.assertEqual(response.status_code, 302)

    def test_post_product_api(self):
        response = self.client.post('/products/new/', self.product_to_create)
        self.assertEqual(response.status_code, 302)

    def test_patch_product_api(self):
        response = self.client.patch(
            f'/products/{self.product.id}', self.product_to_edit)
        self.assertEqual(response.status_code, 301)

    def test_delete_product_api(self):
        response = self.client.delete(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 301)
