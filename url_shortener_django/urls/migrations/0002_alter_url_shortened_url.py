# Generated by Django 4.2.6 on 2023-10-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('urls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortened_url',
            field=models.CharField(
                default='cJaHI4cU',
                max_length=8,
                unique=True,
                verbose_name='shortened_url',
            ),
        ),
    ]