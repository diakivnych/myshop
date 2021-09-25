from django.urls import path
from . import views

urlpatterns = [
	# перенаправлення порожньої сторінки на головну
	path('', views.empty_page, name='empty_page'),
	# сторінка конкретного продукту
	path('product/<str:type_of_product>', views.product_page, name='product_page'),
	# сторінка відгуків
	path('product/<str:product_type>/<int:product_id>/comments', views.comments_page, 
		 name='comments_page'),
	# сторінка реєстрації
	path('registration', views.registration_page, name='registration_page'),
	# сторінка авторизації
	path('authorization', views.authorization_page, name='authorization_page'),
	# сторінка кошику
	path('customer/<int:customer_id>/basket', views.basket_page, name='basket_page'),
	# url для виходу з облікового запису
	path('logout', views.logout_page, name='logout_page'),
	# url, що додає продукт до кошику
	path('add_to_basket/<str:product_name>/<int:product_id>', views.add_to_basket, 
		 name='add_to_basket'),
	# url, що видаляє продукт з кошика
	path('del_from_basket/<str:product_name>/<int:product_id>', views.del_from_basket, 
		 name='del_from_basket'),
	# url, що здійснює пошук по ключу
	path('search_by_key', views.search_by_key, name='search_by_key'),
	# сторінка помилок
	path('error/<str:error_type>', views.error_page, name='error_page'),
	# url, що відповідає за покупку продукту
	path('buy_products', views.buy_products, name='buy_products')
]