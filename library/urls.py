#import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from livro.views import Home
from products.views import *
from users.views import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),
    #user management
    path('', include('pages.urls', namespace='pages')),
    path('livro/', include(('livro.urls','livro'))),
    path('accounts/', include('allauth.urls')),
    path('home/', Home, name='index'),
    path('products/',include(('products.urls','products'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
