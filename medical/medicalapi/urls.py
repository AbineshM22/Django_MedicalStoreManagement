from django.urls import path
from . import views

urlpatterns = [
    path('simpleapi', views.simpleapi, name='simple_api'),
    path('login', views.login, name='login_api'),
    path('Medicineinsert/', views.Medicineinsert.as_view()),
    path('Medicinepick/<int:id>', views.Medicinepick.as_view()),
    path('Medicineupdate/<int:id>', views.Medicineupdate.as_view()),
    path('Medicinedelete/<int:id>', views.Medicinedelete.as_view()),
    path('Medicinesearch', views.Medicinesearch.as_view()),
    path('Medicinelist', views.Medicinelist.as_view()),
    
       
]