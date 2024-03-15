from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Profissional
from .form import ProfissionalRegistrationForm
from django.db.models import Q
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def cadastro(request):
    return HttpResponse("Você está na página de cadastro de clientes.")


# Dicionário de sinônimos expandido
DICIONARIO_DE_SINONIMOS = {
    'faxineira': ['faxineira', 'faxinar', 'faxina'],
    'pintor': ['pintor', 'pintura', 'pintar', 'pintando', 'pintou'],
}

def buscar_profissionais(request):
    resultados = None
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']
        consulta = Q()
        sinonimos_faxineira = DICIONARIO_DE_SINONIMOS.get('faxineira', [])
        sinonimos_pintor = DICIONARIO_DE_SINONIMOS.get('pintor', [])
        
        # Verifica os sinônimos de todas as palavras na consulta
        for palavra, sinonimos in DICIONARIO_DE_SINONIMOS.items():
            if any(sinonimo in query for sinonimo in sinonimos):
                if palavra == 'faxineira':
                    consulta |= Q(nome__icontains='faxineira') | Q(area__icontains='faxineira')
                elif palavra == 'pintor':
                    consulta |= Q(nome__icontains='pintor') | Q(area__icontains='pintor')
        
        # Se nenhum resultado for encontrado, defina resultados como uma lista vazia
        resultados = Profissional.objects.filter(consulta) if consulta else []
        
    return render(request, 'find.html', {'resultados': resultados})


def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')  # Redirecionar para alguma página de sucesso
    else:
        form = ProfissionalRegistrationForm()
    return render(request, 'cadastro_profissional.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'sucesso.html')


