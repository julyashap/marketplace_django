from django.urls import path
from users.views import RegistrationView, LoginView, LogoutView, reset_password, ProfileView, ProfileUpdateView, \
    email_confirm
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/', reset_password, name='password_reset'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update/', ProfileUpdateView.as_view(), name='update_user'),
    path('email/confirm/', email_confirm, name='email_confirm'),
]
