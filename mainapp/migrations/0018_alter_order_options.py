# Generated by Django 4.0.4 on 2023-05-20 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-completed', 'finished', '-transaction_id']},
        ),
    ]
