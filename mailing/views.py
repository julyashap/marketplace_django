from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, DetailView
from mailing.models import Client, Message, Newsletter
from django.core.exceptions import ObjectDoesNotExist


class MailingView(TemplateView):
    template_name = 'mailing/mailing_start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if Client.objects.all() and Message.objects.all():
            context['client'] = True
            context['message'] = True
        else:
            context['client'] = False
            context['message'] = False

        return context


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'patronymic', 'comment',)
    success_url = reverse_lazy('mailing:list_client')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'patronymic', 'comment',)
    success_url = reverse_lazy('mailing:list_client')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailing/confirm_delete.html'
    success_url = reverse_lazy('mailing:list_client')


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mailing:list_message')


class MessageListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'body',)
    success_url = reverse_lazy('mailing:list_message')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing/confirm_delete.html'
    success_url = reverse_lazy('mailing:list_message')


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('first_sending', 'periodicity', 'client', 'message',)
    success_url = reverse_lazy('mailing:list_newsletter')


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('first_sending', 'periodicity', 'client', 'message',)
    success_url = reverse_lazy('mailing:list_newsletter')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'mailing/confirm_delete.html'
    success_url = reverse_lazy('mailing:list_newsletter')
