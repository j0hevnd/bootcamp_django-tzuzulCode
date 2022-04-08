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

# Useful functions
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
        """
        Validate that a user log-in successful
        """
        User.objects.create_user(username='testuser1', password='12345')

        self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse("product:index"))

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)


class ProductTestCase(TestCase):

    def setUp(self):
        """
        Create a user, login of user and create data in the database
        """
        User.objects.create_user(username='testuser1', password='12345')
        self.client.login(username='testuser1', password='12345')

        maker = create_maker('Lácteos del campo') # Cualquier parecido con la realidad es pura coincidencia
        category = create_category('Lacteos')

        time = timezone.now() + datetime.timedelta(20) 
        create_product('Leche', 0, 15, maker, category, time) # this product not has expired
        create_product('Pan', 10, 15, maker, category, timezone.now(), False)


    def test_product_not_is_displayed_is_not_login_user(self):
        """
        Validates that the URL is protected and redirects to the login page
        """
        self.client.logout()

        response = self.client.get(reverse("product:index"), follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/')
        self.assertContains(response, 'Log-in', status_code=200)


    def test_no_display_product_not_public_or_not_have_stock(self):
        """
        Should not displayed products if it no have stock or not is public in page index,
        should send the message: 'There are no registered products'
        """
        response = self.client.get(reverse("product:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no registered products', status_code=200)


    def test_not_display_products_if_product_expired(self):
        """
        If product expired, it not whould are displayed
        """
        maker = create_maker('Lácteos del campo')
        category = create_category('Lacteos')
        product = create_product('Galletas', 10, 15, maker, category, timezone.now())

        response = self.client.get(reverse("product:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIs(product.product_expired(), True)
        self.assertQuerysetEqual(response.context['page_obj'], [])

    
    def test_product_detail_not_displayed(self):
        """
        if the product does not comply with the requirements for be displayed, 
        not should see your detail
        """
        product = Product.objects.get(id=1)
        url = reverse("product:detail_product", args=(product.id,))
        response = self.client.get(url)
        self.assertContains(response, 'No product found', status_code=200)


    def test_product_detail(self):
        """
        Shows a product that comply with the all requirements
        """
        time = timezone.now() + datetime.timedelta(20)

        maker = create_maker('Lácteos del campo')
        category = create_category('Lacteos')
        create_product('Helado', 10, 15, maker, category, time)

        product = Product.objects.get(id=3)
        url = reverse("product:detail_product", args=(product.id,))
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name_product)

