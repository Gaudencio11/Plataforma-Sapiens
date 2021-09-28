# Plataforma-Sapiens
Plataforma de Eventos. Desenvolvido em 2021.1 

Ambiente configurado para rodar no heroku e localmente
Para rodar localmente:
- Iniciar e ativar a venv
- Instalar requirements.txt
- comando py manage.py makemigrations
- comando py manage.py migrate
- comando py manage.py runserver
(todos os comandos precisam ser rodados no diretório raiz e com a venv ativada)
Para rodar no heroku:
- configurações iniciais de autenticação do Heroku CLI
- configurar variável DEBUG, SECRET_KEY, ALLOWED_HOSTS, DATABASES
