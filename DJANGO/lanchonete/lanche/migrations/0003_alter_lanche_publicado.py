# Generated by Django 4.2.4 on 2023-10-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lanche', '0002_remove_lanche_funcionario_lanche_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lanche',
            name='publicado',
            field=models.BooleanField(default=True),
        ),
    ]