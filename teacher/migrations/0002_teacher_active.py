# Generated by Django 4.0.5 on 2022-07-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
