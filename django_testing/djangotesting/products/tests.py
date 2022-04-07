import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product, Maker, Category

# Create your tests here.
"""
Encontrar errores
Profesionalismo
TDD (Test-Driven Development)
"""

# class ProductTestCase(TestCase):

#     def test_product_is_public(self):
#         """ """
#         print("Testing success")


def create_maker(manufacturer_name):
    return Maker.objects.create(manufacturer_name=manufacturer_name)

def create_category(product_category):
    return Category.objects.create(product_category=product_category)

def create_product(name, stock, price, manufacturer, product_type, due_date, public=True):
    return Product.objects.create(
        name_product = name,
        stock = stock,
        price = price,
        manufacturer = manufacturer,
        product_type = product_type,
        due_date = due_date,
        public = public
    )


class UserLoginTestCase(TestCase):
    
    def test_login_user(self):
        User.objects.create_user(username='testuser1', password='12345')

        self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse("product:index"))

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)


class ProductTestCase(TestCase):

    def setUp(self):
        User.objects.create_user(username='testuser1', password='12345')
        self.client.login(username='testuser1', password='12345')

        maker = create_maker('Lácteos del campo') # Cualquier parecido con la realidad es pura coincidencia
        category = create_category('Lacteos')

        create_product('Leche', 0, 15, maker, category, timezone.now())
        create_product('Pan', 10, 15, maker, category, timezone.now(), False)


    def test_product_not_is_displayed_is_not_login_user(self):
        self.client.logout()

        response = self.client.get(reverse("product:index"), follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertContains(response, 'Log-in', status_code=200)

    