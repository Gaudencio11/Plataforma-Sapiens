# Generated by Django 3.1.7 on 2021-05-25 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0005_bdcpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, db_column='cpf', max_length=11, verbose_name='cpf'),
        ),
    ]
