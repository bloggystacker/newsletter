from django.contrib import admin
from django.urls import path
from subscribe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
]
