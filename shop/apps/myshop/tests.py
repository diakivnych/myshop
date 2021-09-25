from django.test import TestCase

from myshop.models import Customer

# Create your tests here.

class CustomerTestCase(TestCase):
	def setUp(self):
		Customer.objects.create(first_name='Dima', last_name='Diakivnych', country='Ukraine',
								phone_number='0980935940', email='d.diakivnych@gmail.com')

	def test_customer_first_name(self):
		person = Customer.objects.get(last_name='Diakivnych')
		self.assertEqual(person.first_name, 'Dima')

	def test_customer_country(self):
		person = Customer.objects.get(last_name='Diakivnych')
		self.assertEqual(person.country, 'Ukraine', 'Неправильно виводить країну')

	def test_customer_phone_number(self):
		person = Customer.objects.get(last_name='Diakivnych')
		self.assertEqual(person.phone_number, '0980935940', 'Неправильно зчитує номер')