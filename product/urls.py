from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.categories_list_api_view),
    path('api/v1/categories/<int:id>/', views.categories_detail_api_view),
    path('api/v1/products/', views.products_list_api_view),
    path('api/v1/products/<int:id>/', views.products_detail_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_api_view),
    path('api/v1/products/reviews/', views.products_reviews_api_view),
]