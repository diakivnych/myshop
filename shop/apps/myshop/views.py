from django.shortcuts import render, redirect
from .models import Laptop, Smartphone, Review, Customer, Basket, Session


# page_views

def q_test(x):
	return x

def empty_page(request):
	return redirect('/product/all')

def product_page(request, type_of_product):
	devices = []
	message = ''

	# відобразити всі товари
	if type_of_product == 'all':
		devices = list(Laptop.objects.all()) + list(Smartphone.objects.all())
		message = 'Всі товари:'

	# відобразити лише ноутбуки
	if type_of_product == 'laptops':
		devices = Laptop.objects.all()
		message = 'Ноутбуки:'

	# відобразити лише смартфони
	if type_of_product == 'smartphones':
		devices = Smartphone.objects.all()
		message = 'Смартфони:'

	result = []
	for dev in devices:
		# додавати продукт лише тоді, коли він є на складі
		if dev.in_stock():
			result.append(dev)

	return render(request, 'main.html', {'devices': result, 'Session': Session, 'message': message}) 

# comments_views

def comments_page(request, product_type, product_id):
	# показати сторінку відгуків продукту "Ноутбук"
	if product_type == 'Laptop':
		device = Laptop.objects.get(id=product_id)
	# показати сторінку відгуків продукту "Смартфон"
	if product_type == 'Smartphone':
		device = Smartphone.objects.get(id=product_id)
	

	# додавання нового відгуку
	if request.method == 'POST':
		author = Session.get_name()
		comment = request.POST['text']
		advantages = request.POST['advantages']
		disadvantages = request.POST['disadvantages']
		
		if (len(list(Review.objects.all())) == 0) or (author != Review.objects.last().author) or \
				(comment != Review.objects.last().comment):
			# створення нового відгуку
			new_review = device.comments.create(author=author, comment=comment, advantages=advantages, 
												disadvantages=disadvantages)
			# записати в базу даних новий відгук
			new_review.save()

	# всі коментарі
	comments_all = reversed(list(device.comments.all()))
	
	return render(request, 'comments.html', {'device': device, 'comments': comments_all, 
				  'Session': Session})

# registration_views

def registration_page(request):

	# додавання нового покупця
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		country = request.POST['country']
		phone_number = request.POST['phone_number']
		email = request.POST['email']
		login = request.POST['login']
		# запис хешу паролю в базу даних
		password = Customer.hash(request.POST['password'])

		# створення нового покупця
		new_customer = Customer.objects.create(first_name=first_name, last_name=last_name, 
											   country=country, phone_number=phone_number, 
											   email=email, login=login, password=password,
											   money=100000)
		# записати в базу даних нового покупця
		new_customer.save()
		
		# авторизуватися
		Session.logged(new_customer.id)

		return redirect('/product/all')

	return render(request, 'registration.html')

# authorization_views

def authorization_page(request):

	# авторизація
	if request.method == 'POST':
		login = request.POST['login']
		# обраховано значення хешу паролю, для перевірки чи є такий користувач
		password = Customer.hash(request.POST['password'])
		
		# пошук користувача з вказаним логіном і паролем
		for customer in Customer.objects.all():
			if (customer.login == login) and (password == customer.password):
				# авторизуватися
				Session.logged(customer.id)

		# якщо не існує користувача з таким логіном і паролем, то обновити сторінку
		if not Session.is_customer_authorized():
			return render(request, 'authorization.html')

		return redirect('/product/all')

	return render(request, 'authorization.html')

# logout_views

def logout_page(request):
	# вийти з облікового запису
	Session.logout()

	return redirect('/product/all')

# basket_views

def basket_page(request, customer_id):

	# якщо користувач не авторизований, то повернути сторінку з помилкою
	if not Session.is_customer_authorized():
		return error_page(request, 'not_authorized')

	customer = Customer.objects.get(id=customer_id)
	devices = []
	message = 'Кошик:'
	# сумарна ціна в кошику
	summary_price = 0
	products_from_basket = customer.basket.all()
	
	for product in products_from_basket:
		summary_price += product.get_product_price()
		devices.append([product.get_product(), product.get_product_cnt(), product.get_product_price()])

	return render(request, 'basket.html', {'devices': devices, 'Session': Session, 'message': message,
				  'summary_price': summary_price, 'customer': customer})

def add_to_basket(request, product_name, product_id):
	# якщо не авторизований користувач додає до кошику товар, то повернути помилку
	if not Session.is_customer_authorized():
		return error_page(request, 'not_authorized')

	customer = Customer.objects.get(id=Session.customer_id)
	Basket.to_add(customer, product_name, product_id)

	return redirect(f'/customer/{Session.customer_id}/basket')
		
def del_from_basket(request, product_name, product_id):
	customer = Customer.objects.get(id=Session.customer_id)
	Basket.to_del(customer, product_name, product_id)

	return redirect(f'/customer/{Session.customer_id}/basket')

# search_views

def search_by_key(request):

	if request.method == 'POST':
		key = request.POST['search_key']
		result = []

		devices = list(Laptop.objects.all()) + list(Smartphone.objects.all())
		for dev in devices:
			if dev.in_stock() and dev.name.find(key) != -1:
				result.append(dev)

		message = 'Знайдені товари:'

		return render(request, 'main.html', {'devices': result, 'Session': Session, 'message': message}) 

# error_views

def error_page(request, error_type):

	# відображає помилку
	return render(request, 'error.html', {'Session': Session, 'error_type': error_type})

# buy_products_views

def buy_products(request):

	customer = Customer.objects.get(id=Session.customer_id)

	baskets = customer.basket.all()
	summary_price = 0
	for basket in baskets:
		summary_price += basket.price
		# якщо ціна покупки більше, ніж баланс користувача, то повернути помилку
		if summary_price > customer.money:
			return error_page(request, 'have_not_enough_money')

		dev = basket.get_product()
		# якщо користувач намагається купити більше товарів, ніж на складі, то повернути помилку
		if int(dev.get_cnt_in_stock()) < int(basket.get_product_cnt()):
			return error_page(request, 'not_in_stock')

	# здійснити покупку всіх товарів в кошику
	for basket in baskets:
		dev = basket.get_product()
		dev.buy_products(basket.get_product_cnt())
		while basket.get_product_cnt():
			basket.dec()
		customer.buy_products(summary_price)

	return redirect(f'/customer/{Session.customer_id}/basket')
