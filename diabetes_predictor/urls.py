from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predictor/', include('predictor.urls')),
    path('', lambda request: redirect('predictor/predict/')),  # Redirect root to predictor/predict/
]
