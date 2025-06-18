from django.db.models.fields import return_None
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from .forms import DespesaForm
from .models import Despesa

class DespesaView(TemplateView):
    template_name = 'cadastro_despesa.html'
    context = DespesaForm

    # rederização de formulário
    def get_context_data(self, **kwargs):
        try:
            context = super(DespesaView, self).get_context_data(**kwargs)
            context['form'] = DespesaForm
            return context
        except Exception as e:
            print(e)

    # coleta e salvamento dos dados
    def post(self, request, *args, **kwargs):
        form = DespesaForm(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()


        else:
            print("Formulario invalido")
            return self.render_to_response({'form': form})

class RelatorioView(TemplateView):

    def get_context_data(self, **kwargs):
        template_name = 'relatorios_despesas.html'
        mensal = Despesa.objects.all()
        context = {'mensal': mensal}
