# Generated by Django 3.1.7 on 2021-06-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0002_auto_20210616_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='curso'),
        ),
    ]
