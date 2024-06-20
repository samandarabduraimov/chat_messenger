from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),  # Bosh sahifa uchun chat yo'nalishi
    path('users/', include('users.urls')),  # Foydalanuvchi yo'nalishlari uchun
]
