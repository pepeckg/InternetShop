from django.contrib import admin
from django.urls import path
from products.views import (products_view, product_detail_view,
                            create_product_view, main, main_view, categories_view)
from django.conf.urls.static import static
from InternetShop.settings import MEDIA_URL, MEDIA_ROOT
from users.views import login_view, logout_view, register_view

urlpatterns = [
path('', main),
path('admin/', admin.site.urls),
path('products/', products_view),
path('main_view/', main_view),
path('products/<int:post_id>/', product_detail_view),
path('categories/', categories_view),
path('products/create/', create_product_view),

path('users/login/', login_view),
path('users/logout/', logout_view),
path('users/register/', register_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)