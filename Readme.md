# DjangoWeb1

Projeto em django para permitir cadastrar dados no banco sqlite e posteriormente buscar as informações para exibir na web.

# Funcionalidades

- [x] Cadastro de usuario e produto atraves da area administrativa do django.
- [x] Rotas para navegação entre index, produto, contato.
- [x] Pagina para informar erro no servidor (404, 500).
- [x] Arquivos estaticos para css, js e imagem.

## Pacotes utilizados

```bash
asgiref
autopep8
Django
gunicorn
pycodestyle
pytz
sqlparse
toml
whitenoise
```

Use o gerenciador de pacotes [pip](https://pypi.org/) para instalação, exemplo:

```bash
pip install Django gunicorn whitenoise
```

## Uso do models no django

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')
```
