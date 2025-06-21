from django.views.generic import TemplateView

# Create your views here.
class ShowMainPage(TemplateView):
    template_name = 'core/index.html'
