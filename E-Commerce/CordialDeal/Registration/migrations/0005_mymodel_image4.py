# Generated by Django 2.2.3 on 2019-07-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_mymodel_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='image4',
            field=models.CharField(default=1, max_length=1180),
            preserve_default=False,
        ),
    ]
