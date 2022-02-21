from django.views.generic import TemplateView

# Create your views here.

class HomepageView(TemplateView):
    template_name='home.html'
class AboutpageView(TemplateView):
    template_name='about.html'