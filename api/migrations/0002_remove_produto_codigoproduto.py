# Generated by Django 5.1 on 2024-10-18 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='codigoProduto',
        ),
    ]
