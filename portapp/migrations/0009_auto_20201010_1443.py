# Generated by Django 3.0.5 on 2020-10-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0008_auto_20201005_2235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewPort',
        ),
        migrations.AddField(
            model_name='port',
            name='port_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
