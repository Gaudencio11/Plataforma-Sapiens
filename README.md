# Plataforma-Sapiens
Plataforma de Eventos. Desenvolvido em 2021.1 

Projeto configurado para rodar em ambiente heroku e localmente

= Para rodar localmente:
- Iniciar e ativar a venv
- Instalar requirements.txt
- comando py manage.py makemigrations
- comando py manage.py migrate
- comando py manage.py runserver
- Adicionar email e senha a serem usados em "pagina_pricipal/core/settings/base.py"
(todos os comandos precisam ser rodados no diretório raiz e com a venv ativada)

=Para rodar no heroku:
- configurações iniciais de autenticação do Heroku CLI
- configurar variável DEBUG, SECRET_KEY, ALLOWED_HOSTS, DATABASES
