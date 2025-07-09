# Imobiliary-project

## Sobre o Projeto
Projeto com foco em aprendizado em Python e com o framework Django.

### Sistema de Aluguel de Imóveis (Imobiliária)
Objetivo: Gerenciar o aluguel de imóveis (apartamentos, casas, salas comerciais). O sistema deve permitir o cadastro de imóveis, controle de clientes e de locações. O sistema será utilizado somente por funcionários da Imobiliária. O sistema deve fornecer funcionalidades para gerenciar Funcionários, Quartos, Clientes e Reservas. Não será necessário o desenvolvimento de funcionalidades de gerenciamento de pagamento.

# Como configurar o projeto

1 - Instale o pyhton na sua máquina, atualmente estamos na versão 3.12
2 - No powershell rode:
```py
pip install django
```
3 - Ainda no terminal rode:
```py
python.exe -m pip install --upgrade pip
```
4 - Abra seu editor de código e rode:
instale
```py
pip install -r requirements.txt
```
5 - Rode o projeto com:
```py
py manage.py runserver
```

[biblioteca de icones](https://heroicons.com/)
=

Instalação: [<3](https://pypi.org/project/heroicons/)

# Como configurar o projeto - linux

1 - Instale o pyhton na sua máquina, atualmente estamos na versão 3.12

2 - No terminal crie um ambiente virtual
com o seguinte comando:
```bash
python3 -m venv venv
```
3 - Ainda no terminal, ative o
ambiente virtual:
```bash
source venv/bin/activate
```
4 - No terminal, verifique se está com o 
ambiente virtual ativo:
```bash
(venv) user@name:~/repositorios/imobiliary_project$
``` 
e rode:
```bash
pip install -r requirements.txt
```
5 - Rode o projeto com:
```bash
python3 manage.py runserver
```

6 - Emails:
Verifique se seu email esta com a config de autenticação com duas etapas:<br></br>
```bash
https://myaccount.google.com/security
```

Crie um app:<br></br>
```bash
https://myaccount.google.com/apppasswords
```