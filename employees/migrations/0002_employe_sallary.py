# Generated by Django 2.1.5 on 2019-01-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='sallary',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
