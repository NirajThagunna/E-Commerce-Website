# Generated by Django 2.2.3 on 2019-07-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0007_order_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='url',
            field=models.CharField(default=1, max_length=1500),
            preserve_default=False,
        ),
    ]
