# Generated by Django 5.1.3 on 2024-11-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='gaveta_grande1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_grande2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_grande3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_grande4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_media1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_media2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_media3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_media4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='gaveta_pequena6',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mail',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Correspondência'), (2, 'Encomenda'), (3, 'Encomenda'), (4, 'Encomenda')]),
        ),
    ]