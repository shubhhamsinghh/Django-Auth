
from django.contrib import admin
from django.urls import path, include
from customauth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.home_view, name='home'),
    path('auth/', include('customauth.urls')),
]
