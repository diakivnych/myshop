from django.db import models


class Product(models.Model):

	class Meta():
		abstract = True			

	name = models.CharField(verbose_name='Назва товару', max_length=50)
	price = models.IntegerField('Ціна')
	description = models.TextField(verbose_name='Опис товару', max_length=1000)
	img = models.ImageField(verbose_name='Фотографія')
	country = models.CharField(verbose_name='Країна-виробник товару', max_length=50)
	warranty = models.CharField(verbose_name='Гарантія', max_length=50)
	color = models.CharField(verbose_name='Колір', max_length=50)
	count_in_stock = models.IntegerField('Кількість на складі')

	def __str__(self):
		return self.name

	# метод, що повертає інформацію про даний екземпляр класу
	def info(self):
		res = []
		res.append('Країна-виробник: ' + str(self.country))
		res.append('Гарантія: ' + str(self.warranty))
		res.append('Колір: ' + str(self.color))
		return res

	# метод, що повертає кількість відгуків певного продукту
	def get_cnt_reviews(self):
		return len(list(self.comments.all()))

	# метод, що повертає кількість даного продукту на складі
	def get_cnt_in_stock(self):
		return self.count_in_stock

	# метод, що повертає True, якщо даний продукт є на складі 
	def in_stock(self):
		return self.count_in_stock > 0

	# метод, що забирає зі складу cnt екземплярів цього продукту
	def buy_products(self, cnt):
		self.count_in_stock -= cnt
		self.save()


class Laptop(Product):

	scr_diagonal = models.FloatField(verbose_name='Діагональ экрану', max_length=10)
	processor = models.CharField(verbose_name='Процесор', max_length=50)
	scr_refresh = models.CharField(verbose_name='Частота оновлення екрану', max_length=50)
	network_adapters = models.CharField(verbose_name='Мережеві адаптери', max_length=50)
	battery_characteristics = models.CharField(verbose_name='Характеристики батареї', max_length=50)

	class Meta:
		verbose_name = "Ноутбук"
		verbose_name_plural = "Ноутбуки"

	# метод, що повертає інформацію про даний екземпляр класу
	def info(self):
		res = Product.info(self)
		res.append('Діагональ екрану: ' + str(self.scr_diagonal))
		res.append('Процесор: ' + str(self.processor))
		res.append('Частота оновлення екрану: ' + str(self.scr_refresh))
		res.append('Мережеві адаптери: ' + str(self.network_adapters))
		res.append('Характеристики батареї: ' + str(self.battery_characteristics))
		return res

	def get_class_name(self):
		return 'Laptop'


class Smartphone(Product):

	os = models.CharField(verbose_name='Операційна система', max_length=50)
	scr_diagonal = models.FloatField(verbose_name='Діагональ екрану')
	display_res = models.CharField(verbose_name='Розширення экрану', max_length=50)
	matrix_type = models.CharField(verbose_name='Тип матриці', max_length=40)
	scr_material = models.CharField(verbose_name='Матеріал екрану', max_length=50)
	ram = models.CharField(verbose_name='Оперативна пам\'ять', max_length=10)
	memory = models.CharField(verbose_name='Влаштована пам\'ять', max_length=10) 
	
	class Meta:
		verbose_name = "Смартфон"
		verbose_name_plural = "Смартфони"

	# метод, що повертає інформацію про даний екземпляр класу
	def info(self):
		res = Product.info(self)
		res.append('Операційна система: ' + str(self.os))
		res.append('Діагональ екрану: ' + str(self.scr_diagonal))
		res.append('Розширення екрану: ' + str(self.display_res))
		res.append('Тип матриці: ' + str(self.matrix_type))
		res.append('Матеріал екрану: ' + str(self.scr_material))
		res.append('Оперативна пам\'ять : ' + str(self.ram))
		res.append('Влаштована пам\'ять: ' + str(self.memory))
		return res


	def get_class_name(self):
		return 'Smartphone'


class Review(models.Model):

	author = models.CharField(verbose_name='Автор', max_length=40)
	comment = models.TextField(verbose_name='Коментар', max_length=2000)
	advantages = models.TextField(verbose_name='Переваги', max_length=500)
	disadvantages = models.TextField(verbose_name='Недоліки', max_length=500)
	created = models.DateField(verbose_name='Дата', auto_now_add=True)

	def __str__(self):
		return self.author


class LaptopReview(Review):

	# створено зв'язок між відгуками та ноутбуки
	laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='comments')

	class Meta:
		verbose_name = "Відгук на ноутбук"
		verbose_name_plural = "Відгуки на ноутбуки"



class SmartphoneReview(Review):

	# створено зв'язок між відгуками та смартфонами
	smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE, related_name='comments')

	class Meta:
		verbose_name = "Відгук на смартфон"
		verbose_name_plural = "Відгуки на смартфони"


class Customer(models.Model):

	first_name = models.CharField(verbose_name='Ім\'я', max_length=40)
	last_name = models.CharField(verbose_name='Прізвище', max_length=40)
	country = models.CharField(verbose_name='Країна', max_length=40)
	phone_number = models.CharField(verbose_name='Номер телефону', max_length=40)
	email = models.EmailField(verbose_name='Email', max_length=254)
	login = models.CharField(verbose_name='Логін', max_length=40)
	password = models.CharField(verbose_name='Пароль', max_length=40)
	money = models.IntegerField(verbose_name='Гроші')

	def __str__(self):
		return self.last_name

	class Meta:
		verbose_name = "Покупець"
		verbose_name_plural = "Покупці"

	# статичний метод, що повертає хеш вхідної паролю
	@staticmethod
	def hash(password):
		password = str(password)

		P = 29
		hashes = 0
		index = 0
		for symbol in password:
			hashes += ord(symbol) * pow(P, index)

			index += 1

		return str(hashes)

	# метод, що зменшує баланс покупця на вказану суму
	def buy_products(self, summary_price):
		self.money -= summary_price
		self.save()


class Basket(models.Model):

	# створено зв'язок між кошиком і покупцем
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='basket')

	type_of_product = models.CharField(verbose_name='Тип продукту', max_length=40)
	product_id = models.IntegerField(verbose_name='Id-продукту')
	cnt = models.IntegerField(verbose_name='Кількість продукту')
	price = models.IntegerField(verbose_name='Ціна')

	# метод, що повертає продукт з даного кошику
	def get_product(self):
		if self.type_of_product == 'Smartphone':
			return Smartphone.objects.get(id=self.product_id)
		elif self.type_of_product == 'Laptop':
			return Laptop.objects.get(id=self.product_id)
		else:
			return None

	# метод, що повертає кількість даного продукту в кошику
	def get_product_cnt(self):
		return self.cnt

	# метод, що повертає ціну продуктів в даному кошику
	def get_product_price(self):
		return self.price

	# метод, що збільшує кількість певного продукту на 1 одиницю
	def inc(self):
		self.cnt += 1
		product = self.get_product()
		self.price += product.price
		self.save()
		
	# метод, що зменшує кількість певного продукту на 1 одиницю
	def dec(self):
		self.cnt -= 1
		product = self.get_product()
		self.price -= product.price

		if self.cnt == 0:
			self.delete()
		else:
			self.save()

	# статичний метод, що шукає потрібний кошик і збільшує кількість його продукту на 1
	@staticmethod
	def to_add(customer, dev_to_add_name, dev_to_add_id):
		baskets = customer.basket.all()

		for basket in baskets:
			dev = basket.get_product()
			if (int(dev_to_add_id) == dev.id) and (dev_to_add_name == dev.get_class_name()):
				basket.inc()
				return

		price = 0
		if dev_to_add_name == 'Laptop':
			price = (Laptop.objects.get(id=dev_to_add_id)).price
		if dev_to_add_name == 'Smartphone':
			price = (Smartphone.objects.get(id=dev_to_add_id)).price

		new_basket = customer.basket.create(type_of_product=dev_to_add_name, product_id=dev_to_add_id, 
					 						cnt=1, price=price)
		new_basket.save()

	# статичний метод, що шукає потрібний кошик і кількіст його продукту на 1
	@staticmethod
	def to_del(customer, dev_to_del_name, dev_to_del_id):
		baskets = customer.basket.all()

		for basket in baskets:
			dev = basket.get_product()
			if (int(dev_to_del_id) == dev.id) and (dev_to_del_name == dev.get_class_name()):
				basket.dec()
				
	class Meta:
		verbose_name = "Кошик"
		verbose_name_plural = "Кошики"


class Session(models.Model):

	# id покупця
	customer_id = int(0)
	# змінна, що показує авторизований покупець чи ні
	is_authorized = False

	# класовий метод, що здійснює авторизацію користувача
	@classmethod
	def logged(cls, customer_id):
		cls.customer_id = customer_id
		cls.is_authorized = True

	# класовий метод, що завершує поточну сесію користувача
	@classmethod
	def logout(cls):
		cls.customer_id = 0
		cls.is_authorized = False

	# класовий метод, що показує чи авторизований користувач зараз на сайті
	@classmethod
	def is_customer_authorized(cls):
		return cls.is_authorized == True

	# класовий метод, що повертає ім'я поточного користувача
	@classmethod
	def get_name(cls):
		if cls.is_customer_authorized():
			customer = Customer.objects.get(id=cls.customer_id)
			return customer.login
