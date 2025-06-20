from django.db.models.fields import return_None
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import DespesaForm, AvistaForm, AprazoForm, MensalForm
from .models import Despesa
from django.db.models import Sum

class DespesaView(TemplateView):
    template_name = 'cadastro_despesa.html'
    context = DespesaForm, AvistaForm, AprazoForm, MensalForm

    # rederização de formulário
    def get_context_data(self, **kwargs):
        try:
            context = super(DespesaView, self).get_context_data(**kwargs)
            context['form'] = DespesaForm
            context['formAvista'] = AvistaForm
            context['formAprazo'] = AprazoForm
            context['formMensal'] = MensalForm
            return context
        except Exception as e:
            print(e)

    # coleta e salvamento dos dados
    def post(self, request, *args, **kwargs):
        form = DespesaForm(request.POST)
        if form.is_valid():
            print("Formulario valido")
            formulario = form.save()

            if formulario.metodo == 'AV':
                formav = AvistaForm(request.POST)
                formav.avista_despesa = formulario.id
                if formav.is_valid():
                    formav.save()

            elif formulario.metodo == 'AP':
                formap = AprazoForm(request.POST)
                formap.avista_despesa = formulario.id
                if formap.is_valid():
                    formap.save()

            elif form.metodo == 'ME':
                formme = MensalForm(request.POST)
                formme.avista_despesa = formulario.id
                if formme.is_valid():
                    formme.save()

            return self.render_to_response({'form': form})

        else:
            print("Formulario invalido")
            return self.render_to_response({'form': form})

class RelatorioView(ListView):
    model = Despesa
    template_name = 'relatorios_despesas.html'
    context_object_name = 'despesas'

    '''def get_context_data(self, **kwargs):
        template_name = 'relatorios_despesas.html'
        mensal = Despesa.objects.all()
        context = {'mensal': mensal}'''

"""    def get(self, request, *args, **kwargs):
        context = super(RelatorioView, self).get(request, *args, **kwargs)
        total = Despesa.objects.all()
        context["total"] = total
        return self.render_to_response(context)"""

