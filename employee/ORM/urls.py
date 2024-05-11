from django.urls import path
from ORM import views

urlpatterns = [
    path('post/', views.create_employee, name='create_employee'),
    path('create/',views.homepage)
]