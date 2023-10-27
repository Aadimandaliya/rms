from django.contrib import admin
from django.urls import path,include
from rmsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('showdata/',views.showdata, name = 'showdata'),
    path('userlogout/',views.userlogout),
]