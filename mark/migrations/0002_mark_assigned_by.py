# Generated by Django 4.0.5 on 2022-07-07 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_active'),
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='assigned_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher'),
        ),
    ]
