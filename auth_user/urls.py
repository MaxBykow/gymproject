from django.contrib import admin
from django.urls import path, include
from .views import RegisterUser, LoginUser, logout_fun

urlpatterns = [
    path('login/', LoginUser.as_view(), name='log'),
    path('logout/', logout_fun, name='logout'),
    path('register/', RegisterUser.as_view(), name='reg'),
    # path('account/', include('auth_user.urls'), name='account'),
]
