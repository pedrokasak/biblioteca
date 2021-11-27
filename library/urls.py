from django.contrib import admin
from django.urls import path, include
from livro.views import Home
from users.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livro/', include(('livro.urls','livro'))),
    path('home/', Home, name='index'),
    path('user/',login, name='login')
]
