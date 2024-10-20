import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from catalog.services import cache_category_list, cache_product_list


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

        return render(request, 'catalog/contacts.html')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        self.queryset = cache_product_list(self.kwargs.get('pk'))

        return super().get_queryset(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['versions'] = Version.objects.all()

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        form.instance.created_at = datetime.datetime.now()
        form.instance.updated_at = datetime.datetime.now()

        form.instance.user = self.request.user

        formset = self.get_context_data()['formset']

        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.category.pk])


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product

    def test_func(self):
        user = self.request.user

        return user == self.get_object().user or user.has_perms(['catalog.can_unpublish',
                                                                 'catalog.can_change_description',
                                                                 'catalog.can_change_category'])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        form.instance.updated_at = datetime.datetime.now()

        formset = self.get_context_data()['formset']

        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.has_perms(['catalog.can_unpublish', 'catalog.can_change_description',
                                        'catalog.can_change_category']):
            return ProductModeratorForm
        return ProductForm

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.category.pk])


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product

    def test_func(self):
        user = self.request.user

        return user == self.get_object().user or user.has_perm('catalog.delete_product')

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.category.pk])


class CategoryListView(ListView):
    model = Category
    queryset = cache_category_list()
