from django.shortcuts import render, redirect
from django.views.generic import TemplateView


def redirect_home(request):
    return redirect('HomePage')


def home_page(request):
    return render(request, 'HomePage.html')


class BehindHeader(TemplateView):
    template_name = 'shared/_Header.html'

    def get_context_data(self, **kwargs):
        return super(BehindHeader, self).get_context_data(**kwargs)


class BehindFooter(TemplateView):
    template_name = 'shared/_Footer.html'

    def get_context_data(self, **kwargs):
        return super(BehindFooter, self).get_context_data(**kwargs)
