# Generated by Django 3.1.7 on 2021-03-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210318_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades del Empleado',
            },
        ),
    ]
