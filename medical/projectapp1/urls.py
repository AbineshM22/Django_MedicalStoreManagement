from django.contrib import admin
from django.urls import path
from projectapp1 import views
urlpatterns = [

    path('',views.Home,name='homepage'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
    path('update/<int:id>',views.Update_Record,name='update'),
    path('search_product',views.search_product,name='search_product'),
   
]