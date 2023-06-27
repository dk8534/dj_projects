from django.urls import path
from . import views
urlpatterns = [
    path('', views.page_counter_view,name='page_counter')
]