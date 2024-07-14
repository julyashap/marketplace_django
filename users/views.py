from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import RegistrationForm
from users.models import User


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('catalog:product_list')
