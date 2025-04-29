from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from rest_framework_simplejwt.views import (  # 🆕 Importación necesaria
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', lambda request: redirect('api/login/')),
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
