from django.test import TestCase
import unittest
from app.models import Supplier, Product
from suppliers.laskin import plus, plus_complicated

from django.test import Client
from django.urls import reverse
from app.views import productlistview, supplierlistview
client = Client()


class UserAuthTests(TestCase):
    def test_listing_products(self):
        '''Call to product list url returns statuscode 200 but let not enter in'''
        response = client.get(reverse(productlistview))
        self.assertEqual(response.status_code, 200)
        a = False
        content = str(response.content)
        if (content.find("login") > 0):
            a = True
        self.assertEqual(a, True)

        

    def test_listing_suppliers(self):
        '''Call to supplier list url returns statuscode 200 but let not enter in'''
        response = client.get(reverse(supplierlistview))
        self.assertEqual(response.status_code, 200)
        a = False
        content = str(response.content)
        if (content.find("login") > 0):
            a = True
        self.assertEqual(a, True)



# setUp metodi testiluokan alussa määrittää jonkin toimenpiteen tekemisen ennen jokaista jäljempänä määritettyä testiä.

# Luodaan testiluokka
class SupplierModelTests(TestCase):
    def setUp(self):
        Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", 
        address="Kultatie 1", phone="12345567", email="jaakko@kulta.fi", country="Finland")
        
    def test_added_supplier_exists(self):
        """Added supplier exists and can be searched"""
        supplier = Supplier.objects.get(companyname="Test company")
        self.assertEqual(supplier.address, "Kultatie 1")
        self.assertEqual(supplier.country, "Finland")
        self.assertEqual(supplier.phone, "12345567")


class ProductModelTests(TestCase):
    def setUp(self):
        x = Supplier.objects.create(companyname="Test company", contactname="Jaakko Kulta", 
        address="Kultatie 1", phone="12345567", email="jaakko@kulta.fi", country="Finland")
        Product.objects.create(productname="Hillo", packagesize="300g", unitprice=4.1, 
        unitsinstock=100, supplier=x)
        
    def test_added_product_exists(self):
        """Added product exists and can be searched"""
        product = Product.objects.get(unitprice=4.1)
        self.assertEqual(product.productname, "Hillo")



class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen
        self.assertEqual(plus(7, 2), 9)
        self.assertEqual(plus(7.1, 2.7), 9.8)

    def test_plus_complicated(self):
        # testaa että funktio palauttaa suuremman luvun, tai niiden summan jos x on suurempi kuin y
        self.assertEqual(plus_complicated(7, 2), 9)
        self.assertEqual(plus_complicated(2, 7), 7)

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 2), "teppo")


    # TDD - Test Driven Development - ensin kirjoitetaan epäonnistuva testi, sitten toteutetaan funktio joka saa testin onnistumaan, 
    # ja lopuksi refaktoroidaan koodia tarpeen mukaan. Näin varmistetaan että koodi toimii halutulla tavalla ja että kaikki testit menevät läpi.
