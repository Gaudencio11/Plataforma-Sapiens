# Generated by Django 3.1.7 on 2021-07-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0006_auto_20210705_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='program',
            options={'verbose_name': 'Atividade'},
        ),
        migrations.AlterField(
            model_name='program',
            name='hour',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, db_column='cpf', max_length=200, verbose_name='Curso'),
        ),
    ]
