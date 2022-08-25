from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'billing/index.html'
