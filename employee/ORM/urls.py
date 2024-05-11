from django.urls import path
from . import views
from .views import UpdateAPIView,DeleteAPIView,UploadPhotoView

urlpatterns = [
    path('post/', views.create_employee, name='create_employee'),
    path('create/', views.homepage),
    path('get/', views.get_data),
    path('update/<int:id>/', UpdateAPIView.as_view(), name='update_employee'),
    path('getdatapage/', views.employee_data_page, name='employee_data'),
    path('delete/<int:id>/', DeleteAPIView.as_view(), name='delete_employee'),
    path('upload_photo/', UploadPhotoView.as_view(), name='upload_photo'),

]



