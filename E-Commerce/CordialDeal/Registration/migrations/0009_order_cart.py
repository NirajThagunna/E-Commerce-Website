# Generated by Django 2.2.3 on 2019-07-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0008_order_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.CharField(default=1, max_length=1800),
            preserve_default=False,
        ),
    ]
