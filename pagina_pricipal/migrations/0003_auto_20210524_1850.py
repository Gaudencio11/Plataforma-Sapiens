# Generated by Django 3.1.7 on 2021-05-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0002_auto_20210524_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, db_column='cpf', max_length=11),
        ),
    ]
