# Generated by Django 5.0.1 on 2024-01-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=350)),
                ('categoria', models.CharField(max_length=60)),
                ('preco', models.FloatField(default=0.0)),
            ],
        ),
    ]