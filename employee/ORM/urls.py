from django.urls import path
from . import views
from .views import UpdateAPIView

urlpatterns = [
    path('post/', views.create_employee, name='create_employee'),
    path('create/', views.homepage),
    path('get/', views.get_data),
    path('update/<int:id>/', UpdateAPIView.as_view(), name='update_employee'),
    path('getdatapage/', views.employee_data_page, name='employee_data'),

]



