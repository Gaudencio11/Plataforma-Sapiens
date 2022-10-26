# Plataforma Sapiens

![](https://raw.githubusercontent.com/Gaudencio11/Plataforma-Sapiens/main/static/images/favicon.ico)

**Plataforma de Eventos. Desenvolvido em 2021.1** 

![](https://img.shields.io/badge/Django-3-blue) ![](https://img.shields.io/badge/Python-3-blue) ![](https://img.shields.io/badge/Pillow-8.2.0-green) ![](https://img.shields.io/badge/django_allauth-0.44.0-green) ![](https://img.shields.io/badge/psycopg2-newest_version-green)

### Features

- It's basically a system where you can add the meeting links of your event. These links will be represented by cards, where you can put an image, a title, a date and a description. Then you can divide the cards by rooms (by different categories). Also you can divide it by days, if your event demands it.

- All the customization said above can be made by the admin of the site, no need to add the information to the code. It's all saved on the database.

- An Authentication system is present

- You can add a noreply email to recovery and activate users accounts.

- It’s prepared to run on heroku. Just follow the documentation at the end of the file


### Instalation

Initiate venv at the project diretory:

	py venv -m venv
	cd venv/Scripts
	activate
	cd ../..

Install requirements.txt:

	py manage.py -r requirements.txt

Run comands bellow (repeat process may be required) to migrate:

	py manage.py makemigrations
	py manage.py migrate
	py manage.py runserver

As said before, configure `pagina_pricipal/core/settings/base.py` to recieve your own noreply email. :call_me_hand:

#### Usefull documentation:
[Django Docs](https://docs.djangoproject.com/en/4.1/) 

[Heroku Docs](https://devcenter.heroku.com/categories/reference)

Use this code as you want, we hope it can help you :owl:
