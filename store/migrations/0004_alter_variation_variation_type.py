# Generated by Django 4.2.2 on 2023-11-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_type',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100),
        ),
    ]
