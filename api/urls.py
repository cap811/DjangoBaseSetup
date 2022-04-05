from django.urls import path
from . import views

# Paths for the API
urlpatterns = [
    path('', views.getData),
    path('post/', views.postData),
    path('put/<int:pk>/', views.putData),
    path('delete/<int:pk>/', views.deleteData),
]
