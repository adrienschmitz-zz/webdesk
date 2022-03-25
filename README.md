<h1 align="center">
    <a href="https://www.djangoproject.com/"> Django</a>
</h1>
<p align="center"> Um Webdesk em Django</p>

<b>Caracteristicas:</b>

- [x] Chamados com cores conforme o status
- [x] Possibilidade adicionar novos status
- [x] Cadastro de Setores, Locais, Solicitantes, Solicitações, Status
- [ ] Reponsivo
- [ ] Modo noturno
- [ ] Abrir para adicionar e editar chamado na mesma guia da lista de chamados
- [ ] Formulário para adicionar solicitante rapidamente
- [ ] Login para acesso ao site

  <b>Começando</b>

  Ter uma instalação do <a href="https://www.python.org/downloads/release/python-399/"> Python 3.9</a>

- Clone esse repositório.
- No terminal:
  - Ir ao diretório do projeto: cd <diretorio>
  - python3.9 -m venv myvenv
  - Ativar a maquina virtual: myvenv\Scripts\activate
  - Atualizar o pip: pip install --upgrade pip
  - Instalar os requisitos: pip install -r requirements.txt

Esse projeto é feito com Postgres. Caso queira usar outro Gerenciador de Banco de Dados, não esqueça de alterar em settings.py:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',

    - Crie um banco de dados chamado: webdesk2 ou escolha outro nome e mude em DATABASES em settings.py
    - Faça as migrações. No terminal: python manage.py makemigrations
    - python manage.py migrate
    - Crie um super usuario: python manage.py createsuperuser
    - Para rodar o projeto: python manage.py runserver
    - Para acessar o site: No navegador http://127.0.0.1:8000/
    - Para acessar o admin: //127.0.0.1:8000/admin

<b>Tecnologias:</b>

-[Python] (<a href="https://www.python.org/" rel="nofollow">https://www.python.org/</a>)<br/> -[Django] (<a href="https://www.djangoproject.com/" rel="nofollow">https://www.djangoproject.com/</a>)<br/> -[Postgres] (<a href="https://www.postgresql.org/" rel="nofollow">https://www.postgresql.org/</a>)

<b>Screenshots:</b>

 <table style="width:100%">
  <tr>
    <td><h1 align="center">
  <img alt="homepagelight" title="homepagelight Page" src="#"  width="295" height="553" />
</h1></td>
  </tr>
 </table>
 
 
### Author
---

 <img style="border-radius: 50%;" src="screenshots/adrien_logo.png" alt=""/>
 
[![Twitter Badge](https://img.shields.io/badge/-@adrienschmitz-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/adrienschmitz)](https://twitter.com/adrienschmitz) [![Linkedin Badge](https://img.shields.io/badge/-adrienschmitz-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/adrienschmitz/)](https://www.linkedin.com/in/adrienschmitz/) 
[![Gmail Badge](https://img.shields.io/badge/-adriens.schmitz@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:adrien.schmitz@gmail.com)](mailto:adrien.schmitz@gmail.com)

Este projeto esta sobe a licença <a href="#">MIT</a>
