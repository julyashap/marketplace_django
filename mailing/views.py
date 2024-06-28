from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from mailing.models import Client, Message, Newsletter


class MailingView(TemplateView):
    template_name = 'mailing_start.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['client'] = get_object_or_404(Client, pk=1)
        context['message'] = get_object_or_404(Message, pk=1)

        return context


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'patronymic', 'comment',)
    success_url = reverse_lazy('mailing:list_client')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'patronymic', 'comment',)
    success_url = reverse_lazy('mailing:list_client')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'confirm_delete'
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
    template_name = 'confirm_delete'
    success_url = reverse_lazy('mailing:list_message')


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = ('first_sending', 'periodicity', 'client', 'message',)
    success_url = reverse_lazy('mailing:list_newsletter')


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('first_sending', 'periodicity', 'client', 'message',)
    success_url = reverse_lazy('mailing:list_newsletter')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    template_name = 'confirm_delete'
    success_url = reverse_lazy('mailing:list_newsletter')
