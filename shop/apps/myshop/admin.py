from django.contrib import admin

from .models import Laptop, Smartphone
from .models import LaptopReview, SmartphoneReview
from .models import Basket, Customer

admin.site.register(Laptop)
admin.site.register(Smartphone)
admin.site.register(LaptopReview)
admin.site.register(SmartphoneReview)
admin.site.register(Customer)
admin.site.register(Basket)