# Generated by Django 4.2.4 on 2023-10-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbackapp', '0002_fisica_usuario_juridica_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisica',
            name='DataNASC',
            field=models.DateField(),
        ),
    ]