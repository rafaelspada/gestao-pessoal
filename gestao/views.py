from django.views.generic import TemplateView

class DespesaView(TemplateView):
    template_name = 'cadastro_despesa.html'

    def post(self):
        pass