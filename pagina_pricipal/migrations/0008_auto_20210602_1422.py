# Generated by Django 3.1.7 on 2021-06-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_pricipal', '0007_auto_20210524_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutorizedCpfs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(default=1, max_length=11)),
            ],
        ),
        migrations.DeleteModel(
            name='Bdcpf',
        ),
    ]
