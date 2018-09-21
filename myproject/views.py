from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from articles.models import Article

class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()
        return context
