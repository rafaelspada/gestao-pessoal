from django.views.generic import TemplateView
from .forms import DespesaForm

class DespesaView(TemplateView):
    template_name = 'cadastro_despesa.html'
    context = DespesaForm

    def get_context_data(self, **kwargs):
        context = super(DespesaView, self).get_context_data(**kwargs)
        context['form'] = DespesaForm
        return context
