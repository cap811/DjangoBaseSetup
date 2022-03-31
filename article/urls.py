from django.urls import path
from . import views

# View function for the article app
urlpatterns = [
    path('', views.index, name='Home'),
    path('<int:article_id>/', views.detail, name='Article'),
]
    