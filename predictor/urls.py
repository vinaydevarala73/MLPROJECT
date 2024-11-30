from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL mapped to home view
    path('predict/', views.predict_diabetes, name='predict_diabetes'),
]
