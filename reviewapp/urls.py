from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='home'),
    path('<int:primary_key>/', views.specificReview , name='review'),
]