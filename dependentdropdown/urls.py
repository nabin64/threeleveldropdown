
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name ='home'),
    path('Add/Project/',views.ADD_PROJECT, name = 'add_project'),
    # ajax part
    path('ajax/load-district/', views.LOAD_DISTRICT, name = "ajax_load_district"),
    path('ajax/load-local/', views.LOAD_LOCAL, name = "ajax_load_local"),
]
