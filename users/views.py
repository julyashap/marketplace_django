from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, DetailView, UpdateView
from users.forms import RegistrationForm, ProfileUpdateForm
from users.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        send_mail('Подтверждение регистрации Skystore',
                  'Здравствуйте! Это письмо - проверка на подлинность '
                  'Вашей электронной почты. Можете на него не отвечать :)',
                  settings.EMAIL_HOST_USER,
                  [self.request.POST.get('email')],
                  fail_silently=True)

        return super().form_valid(form)


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)

            user.set_password(
                get_random_string(length=8)
            )
            user.save()

            send_mail('Новый пароль Skystore',
                      f'Ваш новый пароль: {user.password}',
                      settings.EMAIL_HOST_USER,
                      [email],
                      fail_silently=True)

            return redirect('catalog:product_list')
    else:
        form = PasswordResetForm()

    return render(request, 'users/password_reset.html', {'form': form})


class ProfileView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/update_profile.html'

    def get_object(self, queryset=None):
        return self.request.user
