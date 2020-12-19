from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    # print(dir(request))
    # print(f" Metodo: {request.headers}")
    # print(f" User Agent: {request.headers['User-Agent']}")
    # print(f" User: {request.user} Sobrenome: {request.user.last_name} Email: {request.user.email}")
    # if str(request.user) == 'AnonymousUser':
    #     teste = 'Usuario nao logado.'
    # else:
    #    teste = 'Usuario logado.'
    produtos = Produto.objects.all()

    context = {'curso': 'Programacao Web Django Framework',
               'outro': 'Django � massa!!',
               'produtos': produtos}
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {'prod': prod}
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)