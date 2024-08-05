from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

app_name = 'api'

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('products/<slug:product_slug>/', views.product_detail, name='product_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)