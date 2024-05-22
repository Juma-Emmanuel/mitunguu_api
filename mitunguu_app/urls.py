from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
from django.urls import path

app_name = "mitunguu_app"
urlpatterns = [
    path("authenticate/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('user-register/', UserRegistrationView.as_view(), name='cust-registration-api'),
    path('users/', UsersView.as_view(), name='users-list'),
    path('current-user/', UserDetailsView.as_view(), name='current-user'),
    path('post-product/', ProductCreateView.as_view(), name='post-product'),
    path('products/', GetProductView.as_view(), name='products'),
]
