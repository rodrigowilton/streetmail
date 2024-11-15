# Generated by Django 5.1.3 on 2024-11-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morador', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('recebeu', models.BooleanField(default=False)),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
