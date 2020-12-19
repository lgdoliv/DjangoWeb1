# DjangoWeb1

Projeto em django para buscar informa��es do banco de dados e exibir na web.

# Funcionalidades

- [x] as informa��es podem ser gerenciadas pelo django-admin.
- [x] as informa��es podem ser gerenciadas pelo django-admin.
- [x] as informa��es podem ser gerenciadas pelo django-admin.
- [x] as informa��es podem ser gerenciadas pelo django-admin.
- [x] as informa��es podem ser gerenciadas pelo django-admin.
- [x] as informa��es podem ser gerenciadas pelo django-admin.

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

Use o gerenciador de pacotes [pip](https://pypi.org/) para instala��o, exemplo:

```bash
pip install Django gunicorn whitenoise
```

## Uso do models do pacote django

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Pre�o', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')
```
