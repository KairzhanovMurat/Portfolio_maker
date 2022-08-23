from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib import messages
from .forms import ContactForm


# Create your views here.

class IndexView(generic.TemplateView):

    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        testimonials = models.Testimonial.objects.filter(is_active=True)
        certificates = models.Certificate.objects.filter(is_active=True)
        blogs = models.Blog.objects.filter(is_active=True)
        portfolio = models.Portfolio.objects.filter(is_active=True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio

        return context


class ContactView(generic.FormView):

    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Thank you for filling the form. We will contact with you soon!')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = models.Portfolio
    template_name = 'main/portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
    model = models.Portfolio
    template_name = 'main/portfolio-detail.html'


class BlogView(generic.ListView):
    model = models.Blog
    template_name = 'main/Blog.html'
    paginate_by = 10
    
    def get_queryset(self):
        return super(BlogView, self).get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    model = models.Blog
    template_name = 'main/Blog-detail.html'


