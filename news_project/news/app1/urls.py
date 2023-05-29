from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('bollywood/',views.bollywood,name='bollywood'),
    path('hollywood/',views.hollywood,name='hollywood'),
    path('political/',views.political,name='political'),
    path('sports/',views.sports,name='sports'),
    path('bussiness/',views.bussiness,name='bussiness'),
    path('brand/',views.brand,name='brand')
]