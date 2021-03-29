from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.core.mail import send_mail
from .models import Lead, Agent
from .forms import LeadModelForm, CustomUserCreationForm

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(TemplateView):
    template_name = "landing.html"

class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A New Lead Has Been Created",
            message="Go to the site to see the new lead",
            from_email="zhiying038@gmail.com",
            recipient_list=["zhiying038@gmail.com"]
        )
        return super(LeadCreateView, self).form_valid(form)

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

class LeadDeleteView(DeleteView):
    template_name = "leads/lead-delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")
