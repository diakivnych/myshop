from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	# префікс url, що відповідає за адміністративну панель
    path('admin/', admin.site.urls),
    # префікс url, що відповідає за наш застосунок
    path('', include('myshop.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)