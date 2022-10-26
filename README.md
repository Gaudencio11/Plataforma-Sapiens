# Plataforma-Sapiens
Plataforma de Eventos. Desenvolvido em 2021.1 

Fui o único desnvolvedor Backend desse projeto, tomando todas as decisões de arquitetura e de estratégias, além de realizar o deploy da aplicação no Heroku e em Servidor Linux Debian.

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
